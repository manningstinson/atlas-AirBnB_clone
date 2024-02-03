#!/usr/bin/python3
"""
Module containing the Place class.
"""


class Place:
    """
    A class to represent a place.

    Attributes:
        city_id (str): The ID of the city.
        user_id (str): The ID of the user.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): Maximum number of guests the place can accommodate.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): List of IDs of amenities associated with  place.
    """

    def __init__(self):
        """Initialize Place with default values."""
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []


if __name__ == "__main__":
    # Example usage or testing
    place = Place()
    print(place.__dict__)  # Print the attributes of the place instance
