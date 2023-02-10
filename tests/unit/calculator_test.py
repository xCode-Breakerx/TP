import sys
import unittest
from unittest import TestCase

from calculator import calculator


class TestCalculator(TestCase):
    def test_add(self):
        self.assertEqual(calculator.Calculator.add(1, 1), 2)  # 1 + 1 = 2
        self.assertEqual(calculator.Calculator.add(1, -2), -1)  # 1 - 2 = -1

        # self.assertEqual(calculator.Calculator.add(1.0, -2.2), -1.2)  # 1 - 2.2 != -1.2, this test should fail due to IEEE standard
        # self.assertEqual(calculator.Calculator.add(decimal.Decimal("1"), decimal.Decimal("-2.2")), decimal.Decimal("-1.2"))  # should pass due to higher precision

        # add together different types
        with self.assertRaises(TypeError):
            calculator.Calculator.add(object, object)

        # add together different types
        with self.assertRaises(TypeError):
            calculator.Calculator.add("", 1)

        # Assume that there is no default params
        with self.assertRaises(TypeError):
            calculator.Calculator.add()

        try:
            self.assertTrue(calculator.Calculator.add(sys.maxsize, sys.maxsize) > 0)  # assert that the runtime can handle large numbers with ease, and it can handle wrapping
        except:
            self.fail()

    def test_subtract(self):
        self.assertEqual(calculator.Calculator.subtract(1, 1), 0)  # 1 - 1 = 0
        self.assertEqual(calculator.Calculator.subtract(1, -2), 3)  # 1 + 2 = 3

        # self.assertNotEqual(calculator.Calculator.subtract(decimal.Decimal("0.5"), decimal.Decimal("2.0**-55")), decimal.Decimal("0.5"))  # should pass due to higher precision
        # self.assertNotEqual(calculator.Calculator.subtract(0.5, 2.0 ** -55), 0.5)  # this test should fail due to IEEE standard

        # add together different types
        with self.assertRaises(TypeError):
            calculator.Calculator.subtract(object, object)

        # add together different types
        with self.assertRaises(TypeError):
            calculator.Calculator.subtract("", 1)

        # Assume that there is no default params
        with self.assertRaises(TypeError):
            calculator.Calculator.subtract()

        try:
            self.assertTrue(calculator.Calculator.subtract(-sys.maxsize, sys.maxsize) < 0)  # assert that the runtime can handle large numbers with ease, and it can handle wrapping
        except:
            self.fail()

    def test_multiply(self):
        self.assertEqual(calculator.Calculator.multiply(1, 1), 1)  # 1 * 1 = 1
        self.assertEqual(calculator.Calculator.multiply(1, -2), -2)  # 1 * -2 = -2

        self.assertEqual(calculator.Calculator.multiply(0.5, 0.25), 0.125)  # 0.5 * 0.25 = 0.125
        # self.assertEqual(calculator.Calculator.multiply(decimal.Decimal("1"), decimal.Decimal("-2.2")), decimal.Decimal("-2.2"))  # should pass due to higher precision

        # add together different types
        with self.assertRaises(TypeError):
            calculator.Calculator.multiply(object, object)

        # add together different types, this should not pass even if python is able to multiply strings
        with self.assertRaises(TypeError):
            calculator.Calculator.multiply("", 1)

        # Assume that there is no default params
        with self.assertRaises(TypeError):
            calculator.Calculator.multiply()

        try:
            self.assertTrue(calculator.Calculator.multiply(sys.maxsize, sys.maxsize) > 0)  # assert that the runtime can handle large numbers with ease, and it can handle wrapping
        except:
            self.fail()

    def test_divide(self):
        self.assertEqual(calculator.Calculator.divide(1, 1), 1)  # 1 / 1 = 1
        self.assertEqual(calculator.Calculator.divide(1, -2), -0.5)  # 1 / -2 = -0.5

        self.assertEqual(calculator.Calculator.divide(0.5, 0.25), 2)  # 0.5 / 0.25 = 2
        # self.assertEqual(calculator.Calculator.divide(decimal.Decimal("0.5"), decimal.Decimal("0.25")), decimal.Decimal("2"))  # should pass due to higher precision

        # add together different types
        with self.assertRaises(TypeError):
            calculator.Calculator.divide(object, object)

        # add together different types
        with self.assertRaises(TypeError):
            calculator.Calculator.divide("", 1)

        # Assume that there is no default params
        with self.assertRaises(TypeError):
            calculator.Calculator.divide()

        try:
            self.assertEqual(calculator.Calculator.divide(sys.maxsize, 2), sys.maxsize / 2)  # assert that the runtime can handle large numbers with ease, and it can handle wrapping
        except:
            self.fail()

    def test_power(self):
        self.assertEqual(calculator.Calculator.power(1, 1), 1 ** 1)  # 1 / 1 = 1
        self.assertEqual(calculator.Calculator.power(1, -2), 1 ** -2)  # 1 / -2 = -0.5

        # add together different types
        with self.assertRaises(TypeError):
            calculator.Calculator.power(object, object)

        # add together different types
        with self.assertRaises(TypeError):
            calculator.Calculator.power("", 1)

        # Assume that there is no default params
        with self.assertRaises(TypeError):
            calculator.Calculator.power()

        # Assume that the supported exponent is integer only
        with self.assertRaises(TypeError):
            self.assertEqual(calculator.Calculator.power(0.5, 0.25), 0.5 ** 0.25)  # 0.5 / 0.25 = 2

        try:
            self.assertEqual(calculator.Calculator.power(sys.maxsize, 2), sys.maxsize ** 2)  # assert that the runtime can handle large numbers with ease, and it can handle wrapping
        except:
            self.fail()

    def test_square_root(self):
        self.assertEqual(calculator.Calculator.square_root(1), 1)  # sqrt(1) = 1
        self.assertEqual(calculator.Calculator.square_root(9), 3)  # sqrt(9) = 3

        # add together different types
        with self.assertRaises(TypeError):
            calculator.Calculator.square_root(object, object)

        # add together different types
        with self.assertRaises(TypeError):
            calculator.Calculator.square_root("", 1)

        # Assume that there is no default params
        with self.assertRaises(TypeError):
            calculator.Calculator.square_root()

        # Assume that the params are verified
        with self.assertRaises(TypeError):
            calculator.Calculator.square_root(-2)  # sqrt is not defined for negative numbers


if __name__ == '__main__':
    unittest.main()
