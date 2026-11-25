#!/usr/bin/env python3
"""R04 read-only GitHub Actions runner. No remote writes, no project promotion."""
from __future__ import annotations
import argparse, json, os, re, subprocess, sys, urllib.request
from pathlib import Path
from stage_pfs_children import stage
from export_pfs_children import archive_kind, digest

PFS='xfraggelpower666x/666PFS_CSM'
MAIN='xfraggelpower666x/666MAIN_BRAIN_MYCEL_SYSTEM'
BRANCH='666MAIN_BRAIN'

def api(path: str, token: str|None):
    url='https://api.github.com/repos/'+MAIN+'/'+path
    h={'Accept':'application/vnd.github+json','User-Agent':'PFS-R04-readonly'}
    if token: h['Authorization']='Bearer '+token
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=90) as res:
        return json.load(res)

def check_main(expected_sha: str, expected_projects: list[str], token: str|None):
    commit=api('commits/'+BRANCH,token)
    sha=commit['sha']
    if sha!=expected_sha: raise ValueError('MAIN_HEAD_DRIFT: abort; never overwrite newer state')
    tree_sha=commit.get('commit',{}).get('tree',{}).get('sha')
    if not isinstance(tree_sha,str) or not re.fullmatch(r'[0-9a-f]{40}',tree_sha):
        raise ValueError('MAIN_TREE_SHA_NOT_VERIFIED')
    tree=api('git/trees/'+tree_sha+'?recursive=1',token)
    if tree.get('truncated'): raise ValueError('MAIN_PROJECT_TREE_TRUNCATED')
    names=sorted({x['path'].split('/')[1] for x in tree['tree'] if x['path'].startswith('PROJECTS/') and len(x['path'].split('/'))>2})
    if names != sorted(expected_projects):
        raise ValueError('MAIN_PROJECT_SET_DRIFT: abort; reinventory needed')
    return names

def run(root:Path, out:Path, inventory:dict, expected_pfs:str, expected_main:str, token:str|None):
    if not re.fullmatch(r'[0-9a-f]{40}',expected_pfs) or not re.fullmatch(r'[0-9a-f]{40}',expected_main):
        raise ValueError('INVALID_PINNED_HEAD')
    sha=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
    if sha!=expected_pfs: raise ValueError('PFS_HEAD_MISMATCH')
    if inventory['authority']['pfs_repo']!=PFS or inventory['authority']['main_brain_repo']!=MAIN:
        raise ValueError('WRONG_AUTHORITY')
    current=check_main(expected_main,inventory['project_existing_names'],token)
    actual={str(p.relative_to(root)).replace(os.sep,'/'):p for p in (root/'children').rglob('*') if p.is_file() and archive_kind(p.name)}
    expected=set(inventory['archives_source_paths'])
    if set(actual)!=expected or len(actual)!=31:raise ValueError('ORIGINAL_ARCHIVE_SET_NOT_31_OR_MISMATCH')
    # Git tracks the original binary content, not just the file names.
    for rel,path in actual.items():
        blob=subprocess.check_output(['git','-C',str(root),'hash-object',rel],text=True).strip()
        orig=subprocess.check_output(['git','-C',str(root),'rev-parse',f'HEAD:{rel}'],text=True).strip()
        if blob!=orig:raise ValueError('GIT_BLOB_MISMATCH '+rel)
    result=stage(root,out,expected_head=expected_pfs)
    # Keep review-only and identity-overlap children physically separate from candidates.
    quarantine={x['child_id'] for x in inventory['children'] if x['source_class']!='ACTIVE'}
    for match in inventory.get('potential_semantic_identity_matches_REVIEW_ONLY',[]):
        quarantine.update(match['pfs_children'])
    quarantine.update(child for child in (x.name for x in out.iterdir() if x.is_dir()) if child in current)
    for child in sorted(p for p in out.iterdir() if p.is_dir()):
        group='QUARANTINE' if child.name in quarantine else 'CANDIDATES'
        dest=out/group/child.name
        dest.parent.mkdir(exist_ok=True)
        child.rename(dest)
    # Explicitly verify all 31 archives are represented in child staging receipts.
    reports=[x for x in result['children'] if x['status']=='STAGED']
    total=sum(x['archive_count'] for x in reports)
    if total!=31: raise ValueError('EXTRACTION_ARCHIVE_COUNT_MISMATCH')
    for p in out.rglob('*'):
        if p.is_symlink():raise ValueError('STAGED_SYMLINK_PRESENT')
        if p.is_file() and archive_kind(p.name):raise ValueError('ARCHIVE_REMAINED_IN_OUTPUT')
    # Per-file rehash against existing extraction manifests.
    verified=0
    for child in list((out/'QUARANTINE').glob('*'))+list((out/'CANDIDATES').glob('*')):
        if not child.is_dir(): continue
        mf=child/'PFS_EXPORT_MANIFEST.json'
        if not mf.exists():continue
        data=json.loads(mf.read_text(encoding='utf8'))
        for ent in data['exported_files']:
            fp=child/ent['path']
            if not fp.is_file() or fp.stat().st_size!=ent['size'] or digest(fp)!=ent['sha256']:
                raise ValueError('FILE_READBACK_MISMATCH '+str(fp))
            verified+=1
    check_main(expected_main,current,token)
    if subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()!=expected_pfs:
        raise ValueError('PFS_HEAD_DRIFT')
    receipt={'schema':'PFS_R04_REAL_ACTIONS_EXTRACTION','status':'LOCAL_STAGE_VALIDATED_NO_PUBLICATION',
        'pfs_head':expected_pfs,'main_head':expected_main,'archives_verified':total,
        'child_directories_staged':len(reports),'files_readback_verified':verified,
        'existing_main_brain_projects_protected':current,'remote_writes':0,
        'no_child_autoload':True,'no_foreign_authority_promotion':True,
        'quarantine_children':sorted(quarantine)}
    (out/'R04_RECEIPT.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    return receipt

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--inventory',type=Path,required=True)
    p.add_argument('--pfs-head',required=True)
    p.add_argument('--main-head',required=True)
    a=p.parse_args()
    try:
        receipt=run(a.repo,a.out,json.loads(a.inventory.read_text(encoding='utf8')),a.pfs_head,a.main_head,os.getenv('MAIN_BRAIN_READ_TOKEN'))
        print(json.dumps(receipt,indent=2,ensure_ascii=False))
    except (ValueError,KeyError,OSError,subprocess.CalledProcessError) as exc:
        print('R04_BLOCKED:',exc,file=sys.stderr)
        return 2
    return 0
if __name__=='__main__':sys.exit(main())
