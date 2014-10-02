import lz4file
import os
import unittest

class TestLZ4File(unittest.TestCase):

    def test_1_write(self):
        lz4file.compressTarDefault('src')
        self.assertTrue(os.path.exists('src.lz4'))
    
    def test_2_file(self):
        testTar = lz4file.openTar('src.lz4')
        count = testTar.getmembers()
        for root, dirs, files in os.walk('src'):
            dircount = 1
            dircount += len(dirs)
            dircount += len(files)
        self.assertEqual(dircount, len(count))
        os.remove('src.lz4')

if __name__ == '__main__':
    unittest.main()
