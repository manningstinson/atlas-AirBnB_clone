#!/usr/bin/python3
"""
Module containing the Review class.
"""


class Review:
    """
    A class to represent a review.

    Attributes:
        place_id (str): The ID of the place.
        user_id (str): The ID of the user.
        text (str): The review text.
    """

    def __init__(self):
        """Initialize Review with default values."""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
