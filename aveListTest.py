import unittest
import aveList

class testAveList(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(aveList.aveList([1,2,3]), 2.0)
        self.assertEqual(aveList.aveList([]), "list not populated")
        self.assertEqual(aveList.aveList(["banana", 1, 2]), "input not numbered list")
        self.assertEqual(aveList.aveList(123), "not a list")
        
if __name__ == '__main__':
    unittest.main()
