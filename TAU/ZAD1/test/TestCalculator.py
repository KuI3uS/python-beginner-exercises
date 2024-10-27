import unittest

from TAU.ZAD1.src.Calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):

    def test_correct_return_type(self):
        num1, num2 = 4.8, 12.2
        self.assertIs(type(17.0), type(add(num1, num2)))

    def test_correct_subtraction_with_negatives_values(self):
        num1, num2 = -15, -8
        self.assertEqual(subtract(num1, num2), -7)

    def test_correct_large_division_result(self):
        num1, num2 = 2, 2500000
        self.assertAlmostEqual(0.0000008, divide(num1, num2), places=7)

    def test_correct_addition(self):
        num1, num2 = 17, 33
        self.assertEqual(add(num1, num2), 50)

    def test_divide_is_not_equal(self):
        num1, num2 = 30, 12
        self.assertNotEqual(5, subtract(num1, num2))

    def test_correct_multiplication_with_float(self):
        num1, num2 = 15.5, 6.7
        self.assertAlmostEqual(103.85, multiply(num1, num2), places=2)

    def test_addition_result_greater_than_zero(self):
        num1, num2 = 44, 66
        self.assertTrue(add(num1, num2) > 0)

    def test_correct_division_with_fraction(self):
        num1, num2 = 9, 20
        self.assertEqual(0.45, divide(num1, num2))

    def test_division_by_zero(self):
        num1, num2 = 55, 0
        self.assertRaises(ValueError, divide, num1, num2)

    def test_correct_addition_with_negatives_values(self):
        num1, num2 = -22, 7
        self.assertEqual(-15, add(num1, num2))

    def test_doesnt_return_wrong_type(self):
        num1, num2 = 12.12, 8.88
        self.assertIsNot(type({}), type(add(num1, num2)))


if __name__ == '__main__':
    unittest.main()