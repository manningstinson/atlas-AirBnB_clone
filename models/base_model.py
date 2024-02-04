#!/usr/bin/python3
"""
BaseModel class for common attributes/methods.
"""

import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel  # Import BaseModel directly from base_model module


class BaseModel:
    """
    BaseModel class for common attributes/methods.

    Attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): Datetime representing the creation time.
        updated_at (datetime): Datetime representing the last update time.
    """

    def __init__(self, *args, **kwargs):
        """Initialize instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k in ('created_at', 'updated_at'):
                        setattr(self, k, datetime.strptime(
                            v, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, k, v)
        if not kwargs:
            storage.new(self)

    def __str__(self):
        """Return string representation."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary representation."""
        d = self.__dict__.copy()
        d['__class__'] = type(self).__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d

    def reload_from_dict(self, dictionary):
        """Reload attributes from dictionary representation."""
        for key, value in dictionary.items():
            if key != '__class__':
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
