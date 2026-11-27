import {test} from "node:test";
import assert from "node:assert/strict";
import {publishPfs} from "./r07_production_publisher.mjs";
const A="a".repeat(40), B="b".repeat(40), backup="backup/pfs-r07-test";
const req={expected:A,target:B,approvedTarget:B,backup,phase:"body"};
function setup(files=[{filename:"tools/r07_writer.py",status:"added"}]){
 let current=A, writes=0;
 return {get writes(){return writes},fetch_commit:async ({commit_sha})=>({result:{commit:{sha:commit_sha==="main"?current:A}}}),
 compare_commits:async()=>({result:{files,too_large:false}}),
 update_ref:async args=>{assert.equal(args.force,false);assert.equal(args.expected_sha,A);assert.equal(args.branch_name,"main");writes++;current=B;return {result:{success:true}}}};
}
test("body publication",async()=>{const h=setup();assert.equal(await publishPfs(h,req),B);assert.equal(h.writes,1)});
test("foreign path denied",async()=>{const h=setup([{filename:"children/x",status:"added"}]);await assert.rejects(publishPfs(h,req),/BODY_SCOPE/);assert.equal(h.writes,0)});
test("modified body denied",async()=>{const h=setup([{filename:"tools/r07_writer.py",status:"modified"}]);await assert.rejects(publishPfs(h,req),/BODY_SCOPE/)});
test("pointer only",async()=>{const h=setup([{filename:"registry/CURRENT_POINTER.md",status:"modified"}]);assert.equal(await publishPfs(h,{...req,phase:"pointer"}),B)});
test("mixed pointer denied",async()=>{const h=setup();await assert.rejects(publishPfs(h,{...req,phase:"pointer"}),/POINTER_NOT_LAST/)});
test("unapproved target denied",async()=>{const h=setup();await assert.rejects(publishPfs(h,{...req,approvedTarget:A}),/UNAPPROVED/)});
test("backup mismatch",async()=>{const h=setup();h.fetch_commit=async({commit_sha})=>({result:{commit:{sha:commit_sha==="main"?A:B}}});await assert.rejects(publishPfs(h,req),/BACKUP_MISMATCH/)});
test("CAS rejection",async()=>{const h=setup();h.update_ref=async()=>({result:{success:false}});await assert.rejects(publishPfs(h,req),/CAS_REJECTED/)});
test("readback mismatch",async()=>{const h=setup();h.update_ref=async()=>({result:{success:true}});await assert.rejects(publishPfs(h,req),/READBACK_PENDING/)});
