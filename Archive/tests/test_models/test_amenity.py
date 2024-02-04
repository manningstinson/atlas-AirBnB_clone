#!/usr/bin/python3
"""
Unit tests for the Amenity class.
"""
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def test_init(self):
        """Test initialization of Amenity."""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertEqual(amenity.name, "")

    def test_str(self):
        """Test string representation."""
        amenity = Amenity()
        self.assertEqual(str(amenity), "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__))

    def test_to_dict(self):
        """Test to_dict method."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], amenity.id)
        self.assertEqual(amenity_dict['created_at'], amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'], amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict['name'], amenity.name)


if __name__ == '__main__':
    unittest.main()
