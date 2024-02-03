#!/usr/bin/python3
"""
Unit tests for the City class.
"""
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class."""

    def test_init(self):
        """Test initialization of City."""
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_str(self):
        """Test string representation."""
        city = City()
        self.assertEqual(str(city), "[City] ({}) {}".format(city.id, city.__dict__))

    def test_to_dict(self):
        """Test to_dict method."""
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['id'], city.id)
        self.assertEqual(city_dict['created_at'], city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'], city.updated_at.isoformat())
        self.assertEqual(city_dict['state_id'], city.state_id)
        self.assertEqual(city_dict['name'], city.name)


if __name__ == '__main__':
    unittest.main()
