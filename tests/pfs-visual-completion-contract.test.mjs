import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const contract=readFileSync('governance/PFS_NATIVE_VISUAL_CONTINUATION_CONTRACT_V1.md','utf8');
const skill=readFileSync('666pfs-plugin/current/source/skills/666pfs-visual-interface/SKILL.md','utf8');
for(const token of ['SLOT_1=','SLOT_2=','SLOT_3=','SLOT_4=','SLOT_5=','GUARD_STAGE=','REQUIRED=','BLOCK_IF=','NO_UNSUPPORTED_COMMANDS=TRUE','VISUAL_ENGINE_REUSE=666pfs-visual-interface','NO_FAKE_BUTTONS=TRUE']) assert.ok(contract.includes(token), 'missing visual contract token: '+token);
for(const token of ['exact return anchor','never fake buttons','not another visual engine']) assert.ok(skill.toLowerCase().includes(token), 'missing visual skill guard: '+token);
const options=[1,2,3,4,5].map(n=>contract.match(new RegExp('^SLOT_'+n+'=(.+)$','m'))?.[1]);assert.ok(options.every(Boolean));assert.equal(new Set(options).size,5);
assert.ok(!contract.includes('HOST_ACCEPTANCE=PASS'));console.log('PFS native visual completion contract: PASS (static contract checks only)');
