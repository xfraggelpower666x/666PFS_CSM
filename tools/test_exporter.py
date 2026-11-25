import importlib.util, tempfile, zipfile, json, unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('exporter',Path(__file__).with_name('export_pfs_children.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class T(unittest.TestCase):
 def test_archive_and_nested(self):
  with tempfile.TemporaryDirectory() as d:
   base=Path(d);inside=base/'inside.zip'
   with zipfile.ZipFile(inside,'w') as z:z.writestr('src/app.js','console.log(1)')
   outer=base/'outer.zip'
   with zipfile.ZipFile(outer,'w') as z:z.writestr('README.md','ok');z.write(inside,'nested.zip')
   root=base/'output';root.mkdir();ledger=[];stats={'root':root,'files':0,'bytes':0}
   m.extract_archive(outer,root,ledger,stats)
   self.assertEqual((root/'README.md').read_text(),'ok')
   self.assertTrue(list(root.rglob('app.js')))
   self.assertFalse(list(root.rglob('*.zip')))
 def test_zip_slip_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   base=Path(d);z=base/'bad.zip'
   with zipfile.ZipFile(z,'w') as f:f.writestr('../escape.txt','bad')
   with self.assertRaises(ValueError):m.extract_archive(z,base/'out',[],{'root':base/'out','files':0,'bytes':0})
 def test_duplicate_conflict(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);p.joinpath('x').write_bytes(b'a')
   with self.assertRaises(ValueError):m.put_bytes(p/'x',b'b',[],{'root':p,'files':0,'bytes':0},'source')
 def test_existing_target_never_overwritten(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);stage=p/'stage';stage.mkdir();(stage/'payload.txt').write_text('old')
   target=p/'project';target.mkdir();(target/'payload.txt').write_text('CURRENT')
   self.assertEqual(m.publish_only_if_absent(stage,target),'SKIPPED_EXISTING_DESTINATION')
   self.assertEqual((target/'payload.txt').read_text(),'CURRENT')
 def test_new_target_created(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);stage=p/'stage';(stage/'nested').mkdir(parents=True)
   (stage/'nested'/'a.py').write_text('original')
   target=p/'project'
   self.assertEqual(m.publish_only_if_absent(stage,target),'CREATED_NEW_DESTINATION_VERIFIED')
   self.assertEqual((target/'nested'/'a.py').read_text(),'original')
 def test_atomic_directory_collision(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);stage=p/'stage';stage.mkdir();target=p/'project';target.mkdir()
   (target/'do_not_touch').write_text('LATEST')
   self.assertEqual(m.publish_only_if_absent(stage,target),'SKIPPED_EXISTING_DESTINATION')
   self.assertEqual((target/'do_not_touch').read_text(),'LATEST')
 def test_failed_new_target_never_destructively_rolled_back(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d); stage=p/'stage';stage.mkdir()
   # Eine staged Symlink-Datei darf den Transfer abbrechen.
   (stage/'bad_link').symlink_to('absent')
   target=p/'project'
   with self.assertRaises(ValueError):m.publish_only_if_absent(stage,target)
   # Selbst im Fehlerfall wird das neu reservierte Ziel nicht rekursiv geloescht.
   self.assertFalse(target.exists())
 def test_export_complete_receipt_and_hash(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d); stage=p/'staged';stage.mkdir();(stage/'code.py').write_text('real source',encoding='utf8')
   dest=p/'PROJECTS';dest.mkdir();target=dest/'CHILD'
   self.assertEqual(m.publish_only_if_absent(stage,target),'CREATED_NEW_DESTINATION_VERIFIED')
   receipt=json.loads((target/'PFS_EXPORT_COMPLETE.json').read_text())
   self.assertEqual(receipt['file_count'],1)
   self.assertEqual(receipt['status'],'LOCAL_COPY_READBACK_VERIFIED_NOT_GITHUB_PUBLISHED')
   self.assertFalse((target/'PFS_EXPORT_INCOMPLETE.json').exists())
 def test_symlink_projects_folder_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);stage=p/'stage';stage.mkdir();real=p/'real';real.mkdir()
   alias=p/'PROJECTS';alias.symlink_to(real,target_is_directory=True)
   with self.assertRaises(ValueError):m.publish_only_if_absent(stage,alias/'CHILD')
   self.assertFalse((real/'CHILD').exists())
 def test_staged_symlink_rejected_before_destination_creation(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);stage=p/'stage';stage.mkdir();(stage/'bad').symlink_to('missing')
   projects=p/'PROJECTS';projects.mkdir();target=projects/'NEW'
   with self.assertRaises(ValueError):m.publish_only_if_absent(stage,target)
   self.assertFalse(target.exists())
 def test_existing_target_keeps_current_even_if_staging_symlink(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);stage=p/'stage';stage.mkdir();(stage/'bad').symlink_to('missing')
   projects=p/'PROJECTS';projects.mkdir();target=projects/'CHILD';target.mkdir();(target/'CURRENT').write_text('new')
   with self.assertRaises(ValueError):m.publish_only_if_absent(stage,target)
   self.assertEqual((target/'CURRENT').read_text(),'new')
 def test_post_copy_hash_mismatch_keeps_incomplete_marker(self):
  from unittest.mock import patch
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);stage=p/'stage';stage.mkdir();(stage/'src.txt').write_text('safe')
   projects=p/'PROJECTS';projects.mkdir();target=projects/'CHILD'
   original=m.digest
   def mismatched(path):
    if 'PROJECTS' in path.parts:return '0'*64
    return original(path)
   with patch.object(m,'digest',side_effect=mismatched):
    with self.assertRaises(ValueError):m.publish_only_if_absent(stage,target)
   self.assertTrue((target/'PFS_EXPORT_INCOMPLETE.json').exists())
   self.assertFalse((target/'PFS_EXPORT_COMPLETE.json').exists())
   self.assertEqual((target/'src.txt').read_text(),'safe')
 def test_counts(self):
  self.assertEqual(len(m.ACTIVE),28)
  self.assertEqual(len(m.PRESERVED),4)
if __name__=='__main__':unittest.main()
