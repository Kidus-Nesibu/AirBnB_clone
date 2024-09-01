#!/usr/bin/python3
""" This module handles miscellaneous unit testing """

import os
import models
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """
    Class defines a series of test
    for the Airbnb console
    """

    my_model = BaseModel()

    def test_BaseModelTest_1(self):
        """
        This test ascertains the attributes
        value of a given instance in the BaseModel
        """


        my_model_json = self.my_model.to_dict()

        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])

    def test_Save(self):
        """
        This test checks if the updated_at public
        instance attribute is updated by the
        save method
        """
        self.my_model.save()

        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)
    

    def test_str(self):
        """Test method for str representation
        """
        b1 = BaseModel()
        string = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
        self.assertEqual(b1.__str__(), string)


if __name__ == '__main__':
    unittest.main()