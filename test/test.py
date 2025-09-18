import unittest
from src.imageProc import ImageProc
import os
class MyTestCase(unittest.TestCase):
    def test_cvt_img(self):
        proc = ImageProc(None)
        self.assertEqual(len(proc.readImg("Screenshot_20250828-091956.png"))!=0, True)  # add assertion here

    def test_printing_multi_imgs(self):
        directory_path = "./../data/images"
        proc = ImageProc(directory_path)
        proc.readMultiImgs()


if __name__ == '__main__':
    unittest.main()
