#!/usr/bin/python3
"""
Module containing the State class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class for storing state information.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize State instance.

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
        Return string representation of the State instance.

        Returns:
            str: String representation.

        """
        return "[State] ({}) {}".format(self.id, self.__dict__)

    def to_dict(self):
        """
        Return dictionary representation of the State instance.

        Returns:
            dict: Dictionary representation.

        """
        d = super().to_dict()
        d['name'] = self.name
        return d
