#!/usr/bin/python3
"""
Module containing BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class for common attributes/methods.
    """

    def __init__(self, *args, **kwargs):
        """Initialize instance."""
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        setattr(self, k, datetime.strptime(
                            v, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, k, v)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation."""
        d = self.__dict__.copy()
        d['__class__'] = type(self).__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d