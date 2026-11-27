import assert from "node:assert/strict";
import {test} from "node:test";
import {publishProbe, REPO, PROBE} from "./r07_native_host_bridge.mjs";
const A="a".repeat(40), B="b".repeat(40);
function host() {
  let sha=A, writes=0;
  return {get writes(){return writes},fetch_commit:async args=>{
    assert.deepEqual(args,{repo_full_name:REPO,commit_sha:PROBE});
    return {result:{commit:{sha}}};
  },update_ref:async args=>{
    assert.deepEqual(args,{repository_full_name:REPO,branch_name:PROBE,sha:B,expected_sha:A,force:false});
    writes++;sha=B;return {result:{success:true}};
  }};
}
test("module import and publish",async()=>{const h=host();assert.equal(await publishProbe(h,A,B),B);assert.equal(h.writes,1)});
test("stale head",async()=>{const h=host();await assert.rejects(publishProbe(h,B,A),/HEAD_DRIFT/);assert.equal(h.writes,0)});
test("invalid input",async()=>{const h=host();await assert.rejects(publishProbe(h,"bad",B),/INVALID_HEAD/);assert.equal(h.writes,0)});
test("connector rejection",async()=>{const h=host();h.update_ref=async()=>({result:{success:false}});await assert.rejects(publishProbe(h,A,B),/CAS_REJECTED/)});
test("readback mismatch",async()=>{const h=host();h.update_ref=async()=>({result:{success:true}});await assert.rejects(publishProbe(h,A,B),/READBACK_PENDING/)});
