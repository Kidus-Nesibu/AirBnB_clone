#!/usr/bin/python3
"""Base model script """
import uuid
from datetime import datetime
import models


class BaseModel:
    """Class that is inherited from"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """Return stirng Representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """A dictionary representation of the class"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = self.__dict__["created_at"].isoformat()
        dictionary["updated_at"] = self.__dict__["updated_at"].isoformat()
        return dictionary
