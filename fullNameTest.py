import unittest
import fullName

class TestFullName(unittest.TestCase):
    def test_Name(self):
        self.assertEqual(fullName.fullName("Akshat", "Lunia"), "Akshat Lunia")
        self.assertEqual(fullName.fullName(1, 2), "not a string input")
        self.assertEqual(fullName.fullName("1", "2"), "1 2")

if __name__ == '__main__':
    unittest.main()
