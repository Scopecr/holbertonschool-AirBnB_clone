#!/user/bin/python3
""" Unit tests for the BaseModel class."""


import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class.
    """
    def test_create_instance(self):
        """
        Test if a BaseModel instance can be created.
        """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

if __name__ == '__main__':
    unittest.main()
