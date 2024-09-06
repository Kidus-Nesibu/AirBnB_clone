#!/usr/bin/python3
"""This script is the base model"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base model that every thing will inherit from"""
    def __init__(self, *args, **kwargs):

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
                    storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """saves the time that it is created"""
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """Converts the methods into dictionary"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = datetime.now().isoformat()
        dictionary['updated_at'] = datetime.now().isoformat()

        return dictionary
