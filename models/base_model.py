#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    """Base model that every thing will inherit from"""
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """saves the time that it is created"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Converts the methods into dictionary"""
        dictionary = self.__dict__.copy()
        dictionary['class'] = type(self).__name__
        dictionary['created_at'] = datetime.now().isoformat()
        dictionary['updated_at'] = datetime.now().isoformat()
        return dictionary