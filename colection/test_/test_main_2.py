import unittest
from unittest import TestCase
from main2 import discriminant, solution

class Testsolution(TestCase):

    def test_discriminant(self):
        self.assertEqual(discriminant(1, 8, 15), 4)
        self.assertEqual(discriminant(1, 13, 12), 121)

        self.assertNotEqual(discriminant(4, 28, 49), 3.5)
    def test_solution(self):
        self.assertEqual(solution(1, 8, 15), 5.0)
        self.assertEqual(solution(1, 13, 12), 12.0)
        self.assertEqual(solution(4, 28, 49), 3.5)
        self.assertEqual(solution(1, 1, 1), None)

        self.assertNotEqual(solution(1, 8, 15), 4.0)

if __name__ == '__main__':
    unittest.main()