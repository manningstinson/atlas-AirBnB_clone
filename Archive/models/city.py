#!/usr/bin/python3
"""
Module containing the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for storing city information.

    Attributes:
        state_id (str): The ID of the state associated with the city.
        name (str): The name of the city.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize City instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""

        if kwargs:
            for k, v in kwargs.items():
                if k == 'state_id':
                    setattr(self, k, v)
                elif k == 'name':
                    setattr(self, k, v)

    def __str__(self):
        """
        Return string representation of the City instance.

        Returns:
            str: String representation.

        """
        return "[City] ({}) {}".format(self.id, self.__dict__)

    def to_dict(self):
        """
        Return dictionary representation of the City instance.

        Returns:
            dict: Dictionary representation.

        """
        d = super().to_dict()
        d['state_id'] = self.state_id
        d['name'] = self.name
        return d
