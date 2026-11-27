import unittest
from r07_writer import plan, publish
A, B = "a"*40, "b"*40
P = "children/CURES-16001/candidates/R08/source/test.py"
class Adapter:
    def __init__(self, head=A, accept=True, readback=True):
        self.value, self.accept, self.readback = head, accept, readback
        self.calls = 0
    def head(self, repo, branch):
        return self.value
    def compare_and_swap(self, repo, branch, expected, commit, force=False):
        assert not force
        self.calls += 1
        if not self.accept or self.value != expected: return False
        if self.readback: self.value = commit
        return True
class WriterTests(unittest.TestCase):
    def test_add(self): self.assertEqual(plan([(P,A)],lambda _:None)[0]["sha"],A)
    def test_same(self): self.assertEqual(plan([(P,A)],lambda _:A),[])
    def test_conflict(self):
        with self.assertRaisesRegex(ValueError,"CONFLICT"): plan([(P,A)],lambda _:B)
    def test_scope(self):
        with self.assertRaisesRegex(ValueError,"OUTSIDE_SCOPE"): plan([("registry/CURRENT_POINTER.md",A)],lambda _:None)
    def test_traversal(self):
        with self.assertRaisesRegex(ValueError,"OUTSIDE_SCOPE"): plan([("children/CURES-16001/../x",A)],lambda _:None)
    def test_duplicate(self):
        with self.assertRaisesRegex(ValueError,"DUPLICATE"): plan([(P,A),(P,A)],lambda _:None)
    def test_invalid_sha(self):
        with self.assertRaises(ValueError): plan([(P,"bad")],lambda _:None)
    def test_lookup_error(self):
        def bad(_): raise OSError("transport")
        with self.assertRaises(OSError): plan([(P,A)],bad)
    def test_publish(self): self.assertEqual(publish(Adapter(),A,B),B)
    def test_drift(self):
        api=Adapter(B)
        with self.assertRaisesRegex(ValueError,"HEAD_DRIFT"): publish(api,A,B)
        self.assertEqual(api.calls,0)
    def test_rejected(self):
        with self.assertRaisesRegex(ValueError,"CAS_REJECTED"): publish(Adapter(accept=False),A,B)
    def test_readback(self):
        with self.assertRaisesRegex(ValueError,"READBACK_PENDING"): publish(Adapter(readback=False),A,B)
if __name__ == "__main__": unittest.main()
