import unittest
import datetime
import lab

class TestLab(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(lab.calculate_age(2004), datetime.datetime.now().year - 2004)

    def test_case_2(self):
        self.assertEqual(lab.calculate_grade(95), "A")

    def test_case_3(self):
        self.assertEqual(lab.calculate_grade(76), "B+")

    def test_case_4(self):
        self.assertEqual(lab.calculate_grade(70), "B")

    def test_case_5(self):
        self.assertEqual(lab.calculate_grade(67), "C+")

    def test_case_6(self):
        self.assertEqual(lab.calculate_grade(61), "C")

    def test_case_7(self):
        self.assertEqual(lab.calculate_grade(59), "D+")

    def test_case_8(self):
        self.assertEqual(lab.calculate_grade(51), "D")

    def test_case_0(self):
        self.assertEqual(lab.calculate_grade(48), "F")

if __name__ == "__main__":
    unittest.main()
