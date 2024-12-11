import unittest
import lab

class TestLab(unittest.TestCase):
    def test_case_2(self):
        self.assertEqual(lab.calculate_age(2004), 20)
    def test_case_3(self):
        self.assertEqual(lab.calculate_grade(95), "A")

if __name__ == "__main__":
    unittest.main()
