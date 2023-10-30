#!/usr/bin/python3
"""
This module contains unit tests for the BaseModel class in models/base_model.py.
"""

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
