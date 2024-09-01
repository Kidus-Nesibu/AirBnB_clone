#!/usr/bin/python3
"""This script is the base model"""

import uuid
from datetime import datetime


class BaseModel:
    """Base model that every thing will inherit from"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """saves the time that it is created"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts the methods into dictionary"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = datetime.now().isoformat()
        dictionary['updated_at'] = datetime.now().isoformat()

        return dictionary
