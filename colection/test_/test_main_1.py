import unittest
from unittest import TestCase

from main1 import get_name, get_directory, add, documents

class Testgetname(TestCase):

    def test_get_name(self):
        self.assertMultiLineEqual(get_name("10006"), "Аристарх Павлов")

    def test_get_directory(self):
        self.assertMultiLineEqual(get_directory("11-2"), "1")
        self.assertMultiLineEqual(get_directory("5455 028765"), "1")
        self.assertMultiLineEqual(get_directory("10006"), "2")

    def test_add(self):
        add("international passport", "311 020203", "Александр Пушкин", "3")
        self.assertMultiLineEqual(documents[4]["number"], "311 020203")
        # self.assertMultiLineEqual(add("international passport", "311 020203", "Александр Пушкин", "3"), "311 020204")

if __name__ == '__main__':
    unittest.main()