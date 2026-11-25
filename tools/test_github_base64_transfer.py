import base64, io, json, tempfile, unittest, zipfile
from pathlib import Path
from github_base64_transfer import decode_git_blob, git_blob_sha, run, PFS_BASE, MAIN_BASE

def mkzip(files):
    stream=io.BytesIO()
    with zipfile.ZipFile(stream,'w',zipfile.ZIP_DEFLATED) as z:
        for n,data in files.items():z.writestr(n,data)
    return stream.getvalue()

class Tests(unittest.TestCase):
    def setUp(self):
        self.zip=mkzip({'readme.md':b'valid source\n','src/engine.py':b'x = 123\n'})
        self.sha=git_blob_sha(self.zip)
        self.inventory={'authority':{'pfs_repo':'xfraggelpower666x/666PFS_CSM',
            'main_brain_repo':'xfraggelpower666x/666MAIN_BRAIN_MYCEL_SYSTEM',
            'pfs_head':'a'*40,'main_brain_head':'b'*40},
            'project_existing_names':['ExistingMain'],
            'potential_semantic_identity_matches_REVIEW_ONLY':[{'pfs_children':['CHILD_00']}],
            'children':[{'child_id':f'CHILD_{i:02}', 'source_class':'ACTIVE'} for i in range(31)],
            'archives_source_paths':[f'children/CHILD_{i:02}/runtime/source.zip' for i in range(31)]}
        self.ptree=[{'type':'blob','path':p,'sha':self.sha,'size':len(self.zip)} for p in self.inventory['archives_source_paths']]
        self.mtree=[{'type':'blob','path':'PROJECTS/ExistingMain/README.md','sha':'abc','size':10}]
        self.requests=[]
    def fake(self,url,token):
        self.requests.append(url)
        if url.startswith(PFS_BASE+'/git/trees/'):
            return {'tree':self.ptree}
        if url.startswith(MAIN_BASE+'/git/trees/'):
            return {'tree':self.mtree}
        if url.startswith(PFS_BASE+'/git/blobs/'):
            return {'sha':self.sha,'encoding':'base64','content':base64.b64encode(self.zip).decode()}
        raise AssertionError('Unexpected URL '+url)
    def test_git_blob_sha(self):
        self.assertEqual(git_blob_sha(b'hello'), 'b6fc4c620b67d95f953a5c1c1230aaab5db5a1b0')
    def test_decode_blob_and_length(self):
        v={'sha':self.sha,'encoding':'base64','content':base64.b64encode(self.zip).decode()}
        self.assertEqual(decode_git_blob(v,self.sha,len(self.zip)),self.zip)
        with self.assertRaises(ValueError):decode_git_blob(v,self.sha,len(self.zip)+1)
        with self.assertRaises(ValueError):decode_git_blob(v,'wrong',len(self.zip))
    def test_complete_31_and_quarantine(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'new';d=run(self.inventory,p,None,self.fake,check_current=False)
            self.assertEqual(d['verified'],31)
            self.assertEqual(d['failed'],0)
            self.assertEqual(d['status'],'LOCAL_ARCHIVE_EXTRACTION_VERIFIED')
            self.assertTrue((p/'TRANSFER_COMPLETE.json').is_file())
            self.assertFalse((p/'TRANSFER_INCOMPLETE.json').exists())
            self.assertEqual((p/'QUARANTINE/CHILD_00/runtime/EXTRACTED_ARCHIVES/source/readme.md').read_bytes(),b'valid source\n')
            self.assertTrue((p/'CANDIDATES/CHILD_01/runtime/EXTRACTED_ARCHIVES/source/src/engine.py').is_file())
            self.assertFalse((p/'PROJECTS').exists())
            with self.assertRaises(FileExistsError):run(self.inventory,p,None,self.fake,check_current=False)
    def test_crc_corruption_fails_closed(self):
        with tempfile.TemporaryDirectory() as t:
            bad=bytearray(self.zip)
            bad[45]^=0xFF
            blob=bytes(bad);sha=git_blob_sha(blob)
            self.ptree=[dict(x,sha=sha,size=len(blob)) for x in self.ptree]
            def getter(url,token):
                if '/git/blobs/' in url:return {'sha':sha,'encoding':'base64','content':base64.b64encode(blob).decode()}
                return self.fake(url,token)
            r=run(self.inventory,Path(t)/'new',None,getter,check_current=False)
            self.assertEqual(r['failed'],31)
            self.assertTrue((Path(t)/'new'/'TRANSFER_INCOMPLETE.json').is_file())
            self.assertFalse((Path(t)/'new'/'TRANSFER_COMPLETE.json').exists())
    def test_path_traversal_denied(self):
        with tempfile.TemporaryDirectory() as t:
            self.zip=mkzip({'../escape.md':b'WRONG'})
            self.sha=git_blob_sha(self.zip)
            self.ptree=[dict(x,sha=self.sha,size=len(self.zip)) for x in self.ptree]
            r=run(self.inventory,Path(t)/'new',None,self.fake,check_current=False)
            self.assertEqual(r['verified'],0)
            self.assertEqual(r['failed'],31)
            self.assertFalse((Path(t)/'escape.md').exists())
    def test_inventory_missing_archive_fail(self):
        with tempfile.TemporaryDirectory() as t:
            self.ptree=self.ptree[:-1]
            with self.assertRaises(ValueError):run(self.inventory,Path(t)/'new',None,self.fake,check_current=False)
            self.assertFalse((Path(t)/'new').exists())
    def test_source_class_preservation_quarantine(self):
        with tempfile.TemporaryDirectory() as t:
            self.inventory['children'][7]['source_class']='MIGRATED_OUT_HISTORY_ONLY'
            r=run(self.inventory,Path(t)/'new',None,self.fake,check_current=False)
            self.assertIn('CHILD_07',r['quarantine_children'])
            self.assertTrue((Path(t)/'new/QUARANTINE/CHILD_07/runtime/EXTRACTED_ARCHIVES/source/readme.md').is_file())

if __name__=='__main__':unittest.main()
