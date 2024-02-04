#!/usr/bin/python3
"""
Unit tests for the Review class.
"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_default_values(self):
        """Test that attributes are initialized with default values."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()

