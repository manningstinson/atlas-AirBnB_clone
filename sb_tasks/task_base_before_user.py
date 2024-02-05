#!/usr/bin/python3
"""
Module containing the BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        If kwargs is not empty, it recreates the instance
        from the dictionary representation.

        Args:
            *args: Unused
            **kwargs: Dictionary representation of the instance
        """
        if kwargs:
            # Remove __class__ from kwargs
            kwargs.pop('__class__', None)

            # Convert created_at and updated_at strings to datetime objects
            kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            # Set attributes from kwargs
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            # If kwargs is empty, create new instance with
            # id, created_at, and updated_at
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            from models import storage
            storage.new(self)
            storage.save()

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance.

        Converts datetime objects to string format.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
