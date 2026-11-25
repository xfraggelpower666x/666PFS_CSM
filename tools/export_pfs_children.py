#!/usr/bin/env python3
"""Non-destructive PFS children -> 666MAIN_BRAIN/PROJECTS clear-file exporter.
Requires two complete LOCAL git working trees (including Git LFS objects if used).
Does NOT fetch, commit, push, execute child programs, or modify PFS.
"""
from __future__ import annotations
import argparse, hashlib, json, os, shutil, stat, sys, tarfile, tempfile, zipfile
from pathlib import Path, PurePosixPath

ARCHIVE_SUFFIXES = ('.zip', '.tar.gz', '.tgz', '.tar')
UNSUPPORTED_ARCHIVE_SUFFIXES = ('.7z', '.rar', '.gz', '.bz2', '.xz')
SKIP_PARTS = {'.git', '__MACOSX', '__pycache__'}
MAX_TOTAL = 6 * 1024**3
MAX_FILE = 800 * 1024**2
MAX_FILES = 400000

ACTIVE = '''MP3MANAGER-45001 PFSPLUGIN-44001 STREAMCTRL-40001 PHG-3001 UMIP-4001 STREAM-5001 ITRF-6001 CSLO-9001 UCCF-10001 CODEFORGE-11001 DISCORD-14001 CURES-16001 CLINT-17001 MITF-18001 CSOA-22001 3DXINFO-23001 IMRLA-25001 GTCF-26001 CFL-28001 IG-29001 3DXUI-30001 TRACKHUB-32001 CYBERINTRO-38001 CYBERINTROHQ-39001 LYVRADASH-39001 CURSORGEN-41001 CURSORFRAME-42001 BRIDGEGEN-43001'''.split()
PRESERVED = '''SOUNDWAVE-34001 LIGHT-35001 WEBLYVRA-36001 LYVRAPLUGIN-37001'''.split()
MIGRATED_OUT = '''CHATBACKUP-8001 MIRA-27001 SCC-12001'''.split()
HISTORICAL = '''CTIO-7001 LYVRA-DOLMETSCHER-13001 URLMD-15001 ISQF-24001 UDF-19001 ASMIF-20001 ARCHEON-20001 GIFT-21001 CGF-31001'''.split()

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1<<20), b''): h.update(block)
    return h.hexdigest()

def archive_kind(name):
    n=name.lower()
    return next((x for x in ARCHIVE_SUFFIXES if n.endswith(x)), None)

def safe_rel(name):
    name=name.replace('\\','/')
    p=PurePosixPath(name)
    if p.is_absolute() or any(x in {'..','.'} for x in p.parts) or not p.parts or ':' in p.parts[0]:
        raise ValueError(f'Unsafe archive path: {name}')
    if any(s in SKIP_PARTS for s in p.parts): return None
    return Path(*p.parts)

def put_bytes(path,data,ledger,stats,source):
    if len(data)>MAX_FILE: raise ValueError('Archive entry exceeds file size limit')
    stats['bytes']+=len(data);stats['files']+=1
    if stats['bytes']>MAX_TOTAL or stats['files']>MAX_FILES: raise ValueError('Extraction limit exceeded')
    if path.exists():
        if path.is_symlink() or not path.is_file() or path.read_bytes()!=data: raise ValueError(f'Collision: {path}')
        return
    path.parent.mkdir(parents=True,exist_ok=True)
    if any(x.is_symlink() for x in path.parents): raise ValueError('Symlink parent forbidden')
    path.write_bytes(data)
    ledger.append({'path':str(path.relative_to(stats['root'])).replace(os.sep,'/'),'sha256':digest(path),'size':len(data),'source':source})

def extract_archive(source, target, ledger, stats, depth=0):
    if depth>8: raise ValueError('Nested archive depth exceeds limit')
    name=source.name;kind=archive_kind(name)
    if kind is None: raise ValueError('Unsupported archive')
    content=[]
    if kind=='.zip':
        with zipfile.ZipFile(source) as z:
            for info in z.infolist():
                if info.is_dir():continue
                if (info.external_attr>>16)&0o170000 == stat.S_IFLNK: raise ValueError('Symlink in ZIP forbidden')
                r=safe_rel(info.filename)
                if r is None: continue
                if info.file_size>MAX_FILE: raise ValueError('ZIP entry too large')
                content.append((r,z.read(info)))
    else:
        with tarfile.open(source,'r:*') as t:
            for m in t:
                if m.isdir():continue
                if not m.isfile():raise ValueError('Non-regular TAR entry forbidden')
                r=safe_rel(m.name)
                if r is None: continue
                if m.size>MAX_FILE: raise ValueError('TAR entry too large')
                f=t.extractfile(m)
                if f is None:raise ValueError('TAR entry missing data')
                content.append((r,f.read()))
    for rel,data in content:
        if archive_kind(rel.name):
            with tempfile.TemporaryDirectory() as td:
                tmp=Path(td)/rel.name;tmp.write_bytes(data)
                extract_archive(tmp,target/rel.parent/(rel.name.replace('.','_')+'_EXTRACTED'),ledger,stats,depth+1)
        else:
            if rel.name.lower().endswith(UNSUPPORTED_ARCHIVE_SUFFIXES): raise ValueError(f'Unsupported nested archive: {rel}')
            put_bytes(target/rel,data,ledger,stats,f'archive:{name}')

def export_one(source_child, staging, status):
    if not source_child.is_dir():return {'child':source_child.name,'status':'SOURCE_DIRECTORY_MISSING'}
    out=staging/source_child.name;out.mkdir(parents=True,exist_ok=False)
    ledger=[];stats={'root':out,'files':0,'bytes':0};archives=[]
    for src in sorted(source_child.rglob('*')):
        if any(s in SKIP_PARTS for s in src.relative_to(source_child).parts):continue
        if src.is_symlink():raise ValueError(f'Symlink in source forbidden: {src}')
        if not src.is_file():continue
        rel=src.relative_to(source_child)
        if archive_kind(src.name):
            archives.append({'path':rel.as_posix(),'sha256':digest(src),'size':src.stat().st_size})
            name=src.name
            for suffix in ARCHIVE_SUFFIXES:
                if name.lower().endswith(suffix):name=name[:-len(suffix)];break
            dest=out/rel.parent/'EXTRACTED_ARCHIVES'/name
            extract_archive(src,dest,ledger,stats)
        else:
            if src.name.lower().endswith(UNSUPPORTED_ARCHIVE_SUFFIXES):raise ValueError(f'Unsupported source archive: {src}')
            b=src.read_bytes()
            put_bytes(out/rel,b,ledger,stats,f'pfs:{rel.as_posix()}')
    manifest={'schema':'PFS_CHILD_CLEAR_EXPORT_V1','child_id':source_child.name,'pfs_inventory_class':status,
       'authority':'ORIGIN_NATIVE_AUTHORITY_UNCHANGED','source':'PFS_REPOSITORY_SNAPSHOT_NOT_LIVE_PROMOTION',
       'backup_tier':'TERTIARY_RECOVERY_BACKUP_OF_BACKUP',
       'destination_existing_project_priority':'ABSOLUTE_NO_OVERWRITE',
       'archive_count':len(archives),'original_archives':archives,'exported_file_count':len(ledger),
       'exported_files':ledger,'no_archives_in_output':True,'no_child_autoload':True}
    (out/'PFS_EXPORT_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    return {'child':source_child.name,'status':'STAGED','archive_count':len(archives),'exported_files':len(ledger)}

def publish_only_if_absent(staged_child, destination_child):
    """Publish into a missing *local* project, without overwrites or destructive rollback.

    The COMPLETE receipt is written only after file-by-file hash parity. If a
    copy fails, leave an INCOMPLETE marker and all existing files untouched.
    This is *not* a remote GitHub CAS nor native write authorization.
    """
    if staged_child.is_symlink() or not staged_child.is_dir():
        raise ValueError('Invalid or symlinked staged project')
    if destination_child.parent.is_symlink() or not destination_child.parent.is_dir():
        raise ValueError('Destination PROJECTS must be a real directory')
    if (staged_child/'PFS_EXPORT_COMPLETE.json').exists() or (staged_child/'PFS_EXPORT_INCOMPLETE.json').exists():
        raise ValueError('Staging includes reserved publication receipt')
    # Validate all staged members *before* allocating a destination directory.
    staged_files=[]
    for src in sorted(staged_child.rglob('*')):
        if src.is_symlink() or not (src.is_dir() or src.is_file()):
            raise ValueError(f'Unsafe staged entry: {src}')
        if src.is_file():
            staged_files.append((src, src.relative_to(staged_child), digest(src), src.stat().st_size))
    try:
        destination_child.mkdir(mode=0o700)
    except FileExistsError:
        return 'SKIPPED_EXISTING_DESTINATION'
    incomplete=destination_child/'PFS_EXPORT_INCOMPLETE.json'
    incomplete.write_text(json.dumps({'status':'INCOMPLETE_REVIEW_REQUIRED',
       'note':'Failed or interrupted copy; never treat as complete; do not auto-delete.'})+'\n',encoding='utf8')
    verified=[]
    try:
        for src,rel,expected,expected_size in staged_files:
            out=destination_child/rel
            if any(p.is_symlink() for p in out.parents):
                raise ValueError(f'Symlink parent forbidden: {out}')
            out.parent.mkdir(parents=True,exist_ok=True)
            # 'xb' gives exclusive file creation; never clobber a concurrent file.
            with src.open('rb') as inp, out.open('xb') as target:
                shutil.copyfileobj(inp,target)
                target.flush()
                os.fsync(target.fileno())
            if out.stat().st_size != expected_size or digest(out) != expected:
                raise ValueError(f'Post-copy hash/size mismatch: {out}')
            verified.append({'path':rel.as_posix(),'sha256':expected,'size':expected_size})
        # Re-check the staged baseline to detect concurrent staging mutations.
        for src,rel,expected,expected_size in staged_files:
            if not src.is_file() or src.stat().st_size!=expected_size or digest(src)!=expected:
                raise ValueError(f'Staging drift detected: {src}')
        # Mark fully verified only after all destination files passed readback.
        receipt=destination_child/'PFS_EXPORT_COMPLETE.json'
        with receipt.open('x',encoding='utf8') as out:
            json.dump({'schema':'PFS_LOCAL_EXPORT_COMPLETE_V2',
              'status':'LOCAL_COPY_READBACK_VERIFIED_NOT_GITHUB_PUBLISHED',
              'files':verified,'file_count':len(verified),
              'original_authority_unchanged':True,'no_foreign_write':True},out,indent=2)
            out.write('\n')
        incomplete.unlink()
        return 'CREATED_NEW_DESTINATION_VERIFIED'
    except Exception:
        # Preserve all files and incomplete marker for manual recovery.
        # Never delete a project or perform a rollback on potentially foreign data.
        raise

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--pfs',type=Path,required=True,help='Complete local 666PFS_CSM git working tree')
    ap.add_argument('--main-brain',type=Path,required=True,help='Complete local 666MAIN_BRAIN_MYCEL_SYSTEM git working tree')
    ap.add_argument('--apply',action='store_true',help='Write ONLY to local MAIN-BRAIN working tree; NEVER push')
    ap.add_argument('--active-only',action='store_true',help='Only export 28 active children (default: all PFS-stored child directories)')
    args=ap.parse_args()
    pfs=args.pfs.resolve();dest=args.main_brain.resolve()/'PROJECTS'
    if not (pfs/'children/CHILD_INVENTORY.md').is_file():ap.error('Invalid PFS source / inventory missing')
    if not dest.is_dir():ap.error('MAIN BRAIN PROJECTS directory missing')
    stored=sorted(p.name for p in (pfs/'children').iterdir() if p.is_dir() and p.name not in SKIP_PARTS)
    ids=ACTIVE if args.active_only else stored
    present=[x for x in ids if (pfs/'children'/x).is_dir()]
    missing=[x for x in ids if x not in present]
    collisions=[x for x in present if (dest/x).exists()]
    report={'mode':'APPLY_LOCAL' if args.apply else 'DRY_RUN','selected':len(ids),'present':present,'missing':missing,'destination_collisions':collisions,'existing_projects_preserved':True,'existing_destination_policy':'SKIP_NO_OVERWRITE','backup_tier':'TERTIARY_RECOVERY_BACKUP_OF_BACKUP','git_push':False,'active_in_current_inventory':len(ACTIVE)}
    if not args.apply:
        print(json.dumps(report,ensure_ascii=False,indent=2));return 0
    # Bestehende Zielprojekte sind aktuell und werden nicht ersetzt.
    # Bestehende Projekte werden auch nicht als fehlende PFS-Kopien gewertet.
    with tempfile.TemporaryDirectory(prefix='pfs-clear-export-',dir=dest.parent) as td:
        stage=Path(td);results=[]
        todo=[x for x in present if not (dest/x).exists()]
        for x in present:
            if x not in todo:
                results.append({'child':x,'status':'SKIPPED_EXISTING_DESTINATION'})
            else:
                results.append(export_one(pfs/'children'/x,stage,('ACTIVE' if x in ACTIVE else 'PRESERVATION_BACKUP_ONLY' if x in PRESERVED else 'MIGRATED_OUT_HISTORY_ONLY' if x in MIGRATED_OUT else 'HISTORICAL_REVIEW_ONLY' if x in HISTORICAL else 'UNCLASSIFIED_SOURCE_ONLY')))
        # Zielreservierung mit mkdir(exclusive): gegen TOCTOU geschützt.
        for x in todo:
            outcome=publish_only_if_absent(stage/x,dest/x)
            for entry in results:
                if entry['child']==x:
                    entry['status']=outcome
                    break
    report['results']=results;report['status']='LOCAL_EXPORT_ONLY_NOT_GIT_COMMITTED'
    print(json.dumps(report,ensure_ascii=False,indent=2));return 0

if __name__=='__main__':
    try:sys.exit(main())
    except (ValueError,OSError,zipfile.BadZipFile,tarfile.TarError) as e:
        print('EXPORT BLOCKED:',e,file=sys.stderr);sys.exit(2)
