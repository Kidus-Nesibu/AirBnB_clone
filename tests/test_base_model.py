# test_base_model.py
import unittest
from datetime import datetime
from models.tmp_base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    
    def setUp(self):
        """Set up for the tests."""
        self.model = BaseModel()

    def test_initial_id(self):
        """Test that the id attribute is a non-empty string."""
        self.assertIsInstance(self.model.id, str)
        self.assertTrue(len(self.model.id) > 0)

    def test_initial_created_at(self):
        """Test that created_at is a datetime instance."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_initial_updated_at(self):
        """Test that updated_at is a datetime instance."""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test that the save method updates the updated_at attribute."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test that to_dict method returns a correct dictionary representation."""
        dict_repr = self.model.to_dict()
        self.assertEqual(dict_repr["__class__"], "BaseModel")
        self.assertEqual(dict_repr["created_at"], self.model.created_at.isoformat())
        self.assertEqual(dict_repr["updated_at"], self.model.updated_at.isoformat())
        self.assertIn("id", dict_repr)
        self.assertIn("created_at", dict_repr)
        self.assertIn("updated_at", dict_repr)

    def test_str(self):
        """Test the string representation of the BaseModel instance."""
        str_repr = str(self.model)
        self.assertIn(f"[{self.model.__class__.__name__}] ({self.model.id})", str_repr)
        self.assertIn(str(self.model.__dict__), str_repr)

if __name__ == '__main__':
    unittest.main()
