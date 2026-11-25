#!/usr/bin/env python3
"""Nicht-destruktives PFS-Child-Klarquellen-Staging, ohne GitHub-Writes.

Erfordert eine vollständige PFS-Git-Arbeitskopie. Das Zielverzeichnis darf
noch NICHT existieren. Originalarchive bleiben an der Quelle erhalten.
"""
from __future__ import annotations
import argparse, json, sys, subprocess, re
from pathlib import Path
from export_pfs_children import ACTIVE, PRESERVED, MIGRATED_OUT, HISTORICAL, export_one

def classification(name: str) -> str:
    if name in ACTIVE: return "ACTIVE"
    if name in PRESERVED: return "PRESERVATION_BACKUP_ONLY"
    if name in MIGRATED_OUT: return "MIGRATED_OUT_HISTORY_ONLY"
    if name in HISTORICAL: return "HISTORICAL_REVIEW_ONLY"
    return "UNCLASSIFIED_SOURCE_ONLY"

def stage(pfs: Path, out: Path, active_only=False, expected_head=None):
    pfs=pfs.resolve()
    out=out.absolute()
    observed_head=None
    if expected_head is not None:
        if not re.fullmatch(r"[0-9a-f]{40}", expected_head):
            raise ValueError("Expected commit must be a complete 40-character SHA")
        result=subprocess.run(["git", "-C", str(pfs), "rev-parse", "HEAD"], capture_output=True, text=True)
        if result.returncode != 0:
            raise ValueError("Git source HEAD cannot be verified")
        observed_head=result.stdout.strip()
        if observed_head != expected_head:
            raise ValueError("PFS source HEAD differs from the expected commit")
        dirty=subprocess.run(["git", "-C", str(pfs), "status", "--porcelain", "--", "children"],capture_output=True,text=True)
        if dirty.returncode != 0 or dirty.stdout.strip():
            raise ValueError("PFS children working tree is dirty")
    if out.exists() or out.is_symlink():
        raise FileExistsError("Refusing existing staging destination")
    if not (pfs/"children"/"CHILD_INVENTORY.md").is_file():
        raise ValueError("PFS child inventory missing")
    if out == pfs or pfs in out.parents:
        raise ValueError("Destination must not be inside PFS original repository")
    # Never stage inside ANY Git checkout: protect MAIN BRAIN and other projects.
    for ancestor in (out, *out.parents):
        if (ancestor/".git").exists():
            raise ValueError("Staging inside a Git working tree is forbidden")
    children=pfs/"children"
    ids=ACTIVE if active_only else sorted(x.name for x in children.iterdir() if x.is_dir())
    out.mkdir(parents=False,exist_ok=False)
    (out/"STAGING_INCOMPLETE.json").write_text(json.dumps({"status":"INCOMPLETE","original_authority_unchanged":True})+"\n", encoding="utf-8")
    records=[]
    try:
        for child_id in ids:
            source=children/child_id
            if not source.is_dir():
                records.append({"child":child_id,"status":"SOURCE_MISSING"})
                continue
            records.append(export_one(source,out,classification(child_id)))
        if any(r["status"] not in {"STAGED","SOURCE_MISSING"} for r in records):
            raise ValueError("Unexpected export status")
        receipt={"schema":"PFS_CLEAR_SOURCE_STAGING_V1",
                 "status":"LOCAL_CLEAR_SOURCE_STAGING_COMPLETE_NOT_PUBLISHED",
                 "source_repository":"xfraggelpower666x/666PFS_CSM",
                 "source_head":observed_head,
                 "source_head_verified_against_expected":observed_head is not None,
                 "children":records,
                 "existing_main_brain_projects":"UNTOUCHED",
                 "github_writes":0,
                 "archives_copied_to_output":0,
                 "source_originals_untouched":True,
                 "child_autoload":False,
                 "authority_transfer":False}
        (out/"STAGING_COMPLETE.json").write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        (out/"STAGING_INCOMPLETE.json").unlink()
        return receipt
    except BaseException:
        raise

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pfs",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True,help="New staging dir outside all Git repos, MUST NOT exist")
    ap.add_argument("--active-only",action="store_true")
    ap.add_argument("--expected-head",help="40-hex pinned GitHub HEAD; refuses branch drift and dirty children")
    args=ap.parse_args()
    try:
        print(json.dumps(stage(args.pfs,args.out,args.active_only,args.expected_head),indent=2,ensure_ascii=False))
    except (ValueError,OSError,RuntimeError) as e:
        print(f"STAGING BLOCKED: {e}",file=sys.stderr)
        raise SystemExit(2)

if __name__=="__main__": main()
