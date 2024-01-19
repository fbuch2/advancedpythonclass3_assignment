"""
Test the script
"""

import unittest
from scripts.script import FilteringClass


class TestFiltering(unittest.TestCase):
    """
    Class to test the different filters.
    """

    def setUp(self):
        """
        Wrong variables to enter
        """
        self.gross = "AAAA"
        self.genre = "04"
        self.year = "ASD"

    def test_gross(self):
        """
        Test the gross amount is correct
        """
        with self.assertRaises(TypeError):
            FilteringClass.filter_gross(self, self.gross)

    def test_genre(self):
        """
        Test the genre is one of the options
        """
        with self.assertRaises(TypeError):
            FilteringClass.filter_genre(self, self.genre)

    def test_year_type(self):
        """
        Test if the year filter is a number
        """
        with self.assertRaises(TypeError):
            FilteringClass.filter_year(self, self.year)


if __name__ == "__main__":
    unittest.main()
