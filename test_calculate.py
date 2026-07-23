import unittest

from calculate import (
    add,
    calculate,
    divide,
    factorial,
    modulo,
    percentage,
    power,
    reciprocal,
    square_root,
)


class CalculatorTests(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(modulo(10, 3), 1)

    def test_extended_operations(self):
        self.assertEqual(power(2, 8), 256)
        self.assertEqual(square_root(81), 9)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(percentage(25), 0.25)
        self.assertEqual(reciprocal(4), 0.25)

    def test_dispatcher(self):
        self.assertEqual(calculate("+", 1, 2), 3)
        self.assertEqual(calculate("abs", -8), 8)

    def test_invalid_calculations(self):
        with self.assertRaises(ValueError):
            divide(1, 0)
        with self.assertRaises(ValueError):
            square_root(-1)
        with self.assertRaises(ValueError):
            factorial(2.5)
        with self.assertRaises(ValueError):
            reciprocal(0)
        with self.assertRaises(TypeError):
            add("1", 2)


if __name__ == "__main__":
    unittest.main()
