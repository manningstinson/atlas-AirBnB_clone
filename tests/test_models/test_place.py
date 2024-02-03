import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_default_values(self):
        """Test that attributes are initialized with default values."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_set_attributes(self):
        """Test setting attributes of the Place class."""
        place = Place()
        place.city_id = "city123"
        place.user_id = "user123"
        place.name = "Sample Place"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 40.7128
        place.longitude = -74.0060
        place.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(place.city_id, "city123")
        self.assertEqual(place.user_id, "user123")
        self.assertEqual(place.name, "Sample Place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])

if __name__ == "__main__":
    unittest.main()

