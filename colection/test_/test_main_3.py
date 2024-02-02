import unittest
from unittest import TestCase

from main3 import recordsmen, courses, durations, mentors

class Testrecordsmen(TestCase):

    def test_recordsmen(self):
        self.assertIsInstance(recordsmen(courses, mentors, durations), list)

if __name__ == '__main__':
    unittest.main()