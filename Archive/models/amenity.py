#!/usr/bin/python3
"""
Module containing the Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class for storing amenity information.

    Attributes:
        name (str): The name of the amenity.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize Amenity instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        super().__init__(*args, **kwargs)
        self.name = ""

        if kwargs:
            for k, v in kwargs.items():
                if k == 'name':
                    setattr(self, k, v)

    def __str__(self):
        """
        Return string representation of the Amenity instance.

        Returns:
            str: String representation.

        """
        return "[Amenity] ({}) {}".format(self.id, self.__dict__)

    def to_dict(self):
        """
        Return dictionary representation of the Amenity instance.

        Returns:
            dict: Dictionary representation.

        """
        d = super().to_dict()
        d['name'] = self.name
        return d
