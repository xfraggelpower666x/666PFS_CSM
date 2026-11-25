import sys, pathlib, unittest, tempfile
from unittest.mock import patch
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import run_r04

class R04Checks(unittest.TestCase):
    def test_pin_required_full_sha(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(ValueError,'INVALID_PINNED_HEAD'):
                run_r04.run(pathlib.Path(d),pathlib.Path(d)/'new',{},'abc','def',None)
    def test_main_head_drift_aborts(self):
        inv=['EXISTING']
        def fake(path,token):
            if path.startswith('commits/'):return {'sha':'a'*40,'commit':{'tree':{'sha':'c'*40}}}
            raise AssertionError(path)
        with patch.object(run_r04,'api',side_effect=fake):
            with self.assertRaisesRegex(ValueError,'MAIN_HEAD_DRIFT'):
                run_r04.check_main('b'*40,inv,None)
    def test_truncated_main_tree_aborts(self):
        def fake(path,token):
            if path.startswith('commits/'):return {'sha':'a'*40,'commit':{'tree':{'sha':'c'*40}}}
            return {'truncated':True,'tree':[]}
        with patch.object(run_r04,'api',side_effect=fake):
            with self.assertRaisesRegex(ValueError,'TRUNCATED'):
                run_r04.check_main('a'*40,['EXISTING'],None)
    def test_project_set_changed_aborts(self):
        def fake(path,token):
            if path.startswith('commits/'):return {'sha':'a'*40,'commit':{'tree':{'sha':'c'*40}}}
            return {'truncated':False,'tree':[{'path':'PROJECTS/NEW/main.py'}]}
        with patch.object(run_r04,'api',side_effect=fake):
            with self.assertRaisesRegex(ValueError,'MAIN_PROJECT_SET_DRIFT'):
                run_r04.check_main('a'*40,['EXISTING'],None)
    def test_main_tree_request_uses_tree_sha_not_commit_sha(self):
        calls=[]
        def fake(path,token):
            calls.append(path)
            if path.startswith('commits/'):
                return {'sha':'a'*40,'commit':{'tree':{'sha':'c'*40}}}
            if path.startswith('git/trees/'):
                return {'truncated':False,'tree':[{'path':'PROJECTS/EXISTING/main.py'}]}
            raise AssertionError(path)
        with patch.object(run_r04,'api',side_effect=fake):
            self.assertEqual(run_r04.check_main('a'*40,['EXISTING'],None),['EXISTING'])
        self.assertEqual(calls, ['commits/666MAIN_BRAIN','git/trees/'+('c'*40)+'?recursive=1'])

    def test_main_missing_tree_sha_fails_closed(self):
        with patch.object(run_r04,'api',return_value={'sha':'a'*40}):
            with self.assertRaisesRegex(ValueError,'MAIN_TREE_SHA_NOT_VERIFIED'):
                run_r04.check_main('a'*40,['EXISTING'],None)

    def test_workflow_read_only_dispatch(self):
        s=(ROOT/'.github/workflows/pfs-r04-clear-source-readonly.yml').read_text()
        self.assertIn('workflow_dispatch:',s)
        self.assertIn('contents: read',s)
        self.assertNotIn('contents: write',s)
        self.assertNotIn('git push',s)
        self.assertIn('upload_clear_source',s)
        self.assertIn('default: false',s)
        self.assertIn('retention-days: 1',s)

if __name__=='__main__': unittest.main()
