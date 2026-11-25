#!/usr/bin/env python3
"""PFS R03: read-only GitHub REST Base64 -> isolated extracted child-source staging.

Remote writes: NONE. Existing MAIN BRAIN files: NONE touched.
Use GITHUB_TOKEN in environment for private repositories/rate-limits.
This is a locally runnable tool; live GitHub access must be available to run it.
"""
from __future__ import annotations
import argparse, base64, hashlib, json, os, re, sys, tempfile, urllib.parse, urllib.request, zipfile
from pathlib import Path
from export_pfs_children import extract_archive, digest

OWNER_REPO='xfraggelpower666x/666PFS_CSM'
MAIN_REPO='xfraggelpower666x/666MAIN_BRAIN_MYCEL_SYSTEM'
PFS_BASE='https://api.github.com/repos/'+OWNER_REPO
MAIN_BASE='https://api.github.com/repos/'+MAIN_REPO
ID_RE=re.compile(r'^[A-Za-z0-9][A-Za-z0-9_-]{2,80}$')


def git_blob_sha(blob:bytes)->str:
    return hashlib.sha1(f'blob {len(blob)}\0'.encode()+blob).hexdigest()


def github_json(url:str, token:str|None=None)->dict:
    if not url.startswith('https://api.github.com/repos/'):
        raise ValueError('Only GitHub repository REST URLs allowed')
    headers={'Accept':'application/vnd.github+json','User-Agent':'PFS-readonly-clear-source-exporter','X-GitHub-Api-Version':'2022-11-28'}
    if token:headers['Authorization']='Bearer '+token
    req=urllib.request.Request(url,headers=headers,method='GET')
    with urllib.request.urlopen(req,timeout=75) as resp:
        if resp.status!=200:raise RuntimeError(f'GitHub GET status {resp.status}')
        return json.loads(resp.read())


def decode_git_blob(obj:dict,sha:str, expected_size:int)->bytes:
    if obj.get('sha')!=sha or obj.get('encoding')!='base64':
        raise ValueError('Blob identity or content encoding mismatch')
    raw=base64.b64decode(obj['content'],validate=False)
    if len(raw)!=expected_size or git_blob_sha(raw)!=sha:
        raise ValueError('Git binary blob SHA/size readback mismatch')
    return raw


def get_tree(repo_base,head,token):
    info=github_json(f'{repo_base}/git/trees/{head}?recursive=1',token)
    if info.get('truncated'):
        raise ValueError('Tree response truncated: refuse incomplete inventory')
    return info['tree']


def assert_heads(pfs_head:str,main_head:str,token:str|None):
    # Fail closed for stale manifests and moving branches. No HEAD changes are performed.
    pfs=github_json(f'{PFS_BASE}/commits/main',token)['sha']
    main=github_json(f'{MAIN_BASE}/commits/666MAIN_BRAIN',token)['sha']
    if pfs!=pfs_head or main!=main_head:
        raise ValueError('Current repository HEAD differs from pinned inventory: re-inventory first')


def unzip_into(raw:bytes, rel:str, target:Path,ledger:list,stats:dict):
    # ZipFile.testzip checks full CRC, then original extraction implementation
    # rejects path traversal, symlinks, oversized members and nested bad archives.
    if not zipfile.is_zipfile(__import__('io').BytesIO(raw)):
        raise ValueError('Not a valid ZIP container')
    with zipfile.ZipFile(__import__('io').BytesIO(raw)) as z:
        broken=z.testzip()
        if broken:raise ValueError('CRC mismatch for '+broken)
        entries=len(z.infolist())
    with tempfile.TemporaryDirectory(prefix='pfs-archive-') as tmp:
        archive=Path(tmp)/Path(rel).name
        archive.write_bytes(raw)
        extract_archive(archive,target,ledger,stats)
    return entries


def run(inventory:dict, out:Path, token:str|None, get=github_json, check_current=True):
    basis=inventory['authority']
    if basis['pfs_repo']!=OWNER_REPO or basis['main_brain_repo']!=MAIN_REPO:
        raise ValueError('Unexpected authority in inventory')
    pfs_head=basis['pfs_head']; main_head=basis['main_brain_head']
    if check_current:assert_heads(pfs_head,main_head,token)
    pfs_response=get(f'{PFS_BASE}/git/trees/{pfs_head}?recursive=1',token)
    main_response=get(f'{MAIN_BASE}/git/trees/{main_head}?recursive=1',token)
    if pfs_response.get('truncated') or main_response.get('truncated'):
        raise ValueError('Truncated remote tree; full preflight required')
    pfs_tree=pfs_response['tree']; main_tree=main_response['tree']
    # Never trust incomplete tree results.
    main_dirs={x['path'].split('/')[1] for x in main_tree if x['path'].startswith('PROJECTS/') and len(x['path'].split('/'))>=3}
    mandatory=set(inventory['project_existing_names'])
    if not mandatory.issubset(main_dirs):raise ValueError('Protected MAIN-BRAIN project tree mismatch')
    paths={x['path']:x for x in pfs_tree if x.get('type')=='blob' and x['path'].startswith('children/')}
    archive_paths=list(inventory['archives_source_paths'])
    if len(set(archive_paths))!=31 or any(a not in paths for a in archive_paths):
        raise ValueError('31 pinned archive source paths not all present')
    quarantined=set()
    for e in inventory.get('potential_semantic_identity_matches_REVIEW_ONLY',[]):
        quarantined.update(e['pfs_children'])
    # Explicit historic and preservation classes stay isolated even without name conflict.
    for c in inventory['children']:
        if c['source_class']!='ACTIVE':quarantined.add(c['child_id'])
    if out.exists() or out.is_symlink():raise FileExistsError('Destination already exists; refuse overwrite')
    out.mkdir(parents=True,exist_ok=False)
    pending=out/'TRANSFER_INCOMPLETE.json'
    pending.write_text(json.dumps({'status':'INCOMPLETE','no_remote_writes':True})+'\n')
    results=[]
    for path in archive_paths:
        f=paths[path]; child=path.split('/')[1]
        if not ID_RE.fullmatch(child):raise ValueError('Unexpected child identifier')
        rec={'path':path,'child':child,'git_blob_sha':f['sha'],'bytes_expected':f['size'],'status':'READBACK_PENDING'}
        results.append(rec)
        try:
            obj=get(f'{PFS_BASE}/git/blobs/{f["sha"]}',token)
            raw=decode_git_blob(obj,f['sha'],f['size'])
            rec['sha256_original']=hashlib.sha256(raw).hexdigest()
            group='QUARANTINE' if child in quarantined or child in main_dirs else 'CANDIDATES'
            target=out/group/child/Path(path).parent.relative_to(Path('children')/child)/'EXTRACTED_ARCHIVES'/Path(path).stem
            target.mkdir(parents=True,exist_ok=False)
            stats={'root':out,'files':0,'bytes':0}; ledger=[]
            rec['zip_entries']=unzip_into(raw,path,target,ledger,stats)
            rec['files_extracted']=len(ledger)
            rec['extracted_sha256']=ledger
            rec['status']='EXTRACTED_CRC_AND_FILE_SHA_VERIFIED'
            rec['group']=group
        except Exception as e:
            # No rollback, no false claim of complete export; isolate failures.
            rec['status']='READBACK_OR_EXTRACT_FAILED'
            rec['error']=str(e)[:250]
    receipt={'schema':'PFS_GITHUB_BASE64_CLEAR_SOURCE_R03','pfs_head':pfs_head,'main_head':main_head,
             'source_archives':len(archive_paths),
             'verified':sum(x['status']=='EXTRACTED_CRC_AND_FILE_SHA_VERIFIED' for x in results),
             'failed':sum(x['status']!='EXTRACTED_CRC_AND_FILE_SHA_VERIFIED' for x in results),
             'existing_main_projects_untouched':True,'no_remote_writes':True,
             'quarantine_children':sorted(quarantined),'archives':results}
    # A branch move during the transfer invalidates publication readiness.
    # The staging files remain reviewable, but never become a completed transfer.
    if check_current:
        try:
            assert_heads(pfs_head,main_head,token)
        except Exception as drift:
            receipt['head_drift']=str(drift)[:250]
            receipt['failed']+=1
    receipt['status']='LOCAL_ARCHIVE_EXTRACTION_VERIFIED' if receipt['failed']==0 else 'PARTIAL_REVIEW_REQUIRED'
    (out/'TRANSFER_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    if receipt['failed']==0:
        pending.unlink()
        (out/'TRANSFER_COMPLETE.json').write_text(json.dumps({'status':'LOCAL_EXTRACTION_COMPLETE_NOT_GITHUB_PUBLISHED', 'pfs_head':pfs_head,'archive_count':31})+'\n')
    return receipt


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inventory',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    obj=json.loads(args.inventory.read_text(encoding='utf-8'))
    result=run(obj,args.output,os.environ.get('GITHUB_TOKEN'))
    print(json.dumps({k:v for k,v in result.items() if k!='archives'},ensure_ascii=False,indent=2))
    return 0 if result['failed']==0 else 2

if __name__=='__main__':
    try:sys.exit(main())
    except (OSError,ValueError,KeyError,RuntimeError) as e:
        print('TRANSFER BLOCKED:',str(e),file=sys.stderr);sys.exit(2)
