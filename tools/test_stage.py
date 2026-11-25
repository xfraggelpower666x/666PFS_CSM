import tempfile, zipfile, json, unittest
from pathlib import Path
from stage_pfs_children import stage

class StageTests(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup)
        self.base=Path(self.t.name)
        self.pfs=self.base/'pfs';(self.pfs/'children').mkdir(parents=True)
        (self.pfs/'children'/'CHILD_INVENTORY.md').write_text('ACTIVE_REGISTERED=28')
        c=self.pfs/'children'/'3DXINFO-23001';c.mkdir()
        (c/'SYSTEM_IDENTITY.md').write_text('ORIGINAL CONTENT')
        with zipfile.ZipFile(c/'full.zip','w') as z:z.writestr('module.py','print("test")\n')
        self.child=c
    def test_stages_readable_unpacked_original(self):
        o=self.base/'new-stage';r=stage(self.pfs,o)
        self.assertEqual(r['status'],'LOCAL_CLEAR_SOURCE_STAGING_COMPLETE_NOT_PUBLISHED')
        self.assertEqual((o/'3DXINFO-23001'/'SYSTEM_IDENTITY.md').read_text(),'ORIGINAL CONTENT')
        self.assertEqual((o/'3DXINFO-23001'/'EXTRACTED_ARCHIVES'/'full'/'module.py').read_text(),'print("test")\n')
        self.assertFalse(list(o.rglob('*.zip')))
        self.assertTrue((o/'STAGING_COMPLETE.json').is_file())
        self.assertFalse((o/'STAGING_INCOMPLETE.json').exists())
        self.assertEqual((self.child/'SYSTEM_IDENTITY.md').read_text(),'ORIGINAL CONTENT')
    def test_existing_destination_never_written(self):
        o=self.base/'new-stage';o.mkdir();(o/'keep.txt').write_text('CURRENT')
        with self.assertRaises(FileExistsError):stage(self.pfs,o)
        self.assertEqual((o/'keep.txt').read_text(),'CURRENT')
    def test_failed_archive_leaves_incomplete(self):
        (self.child/'full.zip').write_bytes(b'broken')
        o=self.base/'bad-stage'
        with self.assertRaises(zipfile.BadZipFile):stage(self.pfs,o)
        self.assertTrue((o/'STAGING_INCOMPLETE.json').exists())
        self.assertFalse((o/'STAGING_COMPLETE.json').exists())
    def test_any_git_worktree_forbidden(self):
        checkout=self.base/'main_brain'
        checkout.mkdir()
        (checkout/'.git').mkdir()
        (checkout/'PROJECTS').mkdir()
        with self.assertRaises(ValueError):stage(self.pfs,checkout/'PROJECTS'/'new-stage')
        self.assertFalse((checkout/'PROJECTS'/'new-stage').exists())
    def test_outside_pfs_only(self):
        with self.assertRaises(ValueError):stage(self.pfs,self.pfs/'out')

if __name__=='__main__':unittest.main()
