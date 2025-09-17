import unittest
from src.imageProc import ImageProc

class MyTestCase(unittest.TestCase):
    def test_something(self):
        proc = ImageProc(None)
        self.assertEqual(len(proc.readImg("Screenshot_20250828-091956.png"))!=0, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
