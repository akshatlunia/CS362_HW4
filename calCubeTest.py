import unittest
import calcCube

class testCubeCalc(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(calcCube.calcCube(5), 125)
        self.assertEqual(calcCube.calcCube(-5), "undefined")
        self.assertEqual(calcCube.calcCube(0), "undefined")
        self.assertEqual(calcCube.calcCube(1.2), 1.728)

if __name__ == '__main__':
    unittest.main()
