#!/usr/bin/python3
import unittest
from models.place import Place

class TestPlaceMethods(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_city_id(self):
        self.assertIsNone(self.place.city_id)
        self.place.city_id = "test_city"
        self.assertEqual(self.place.city_id, "test_city")

    def test_user_id(self):
        self.assertIsNone(self.place.user_id)
        self.place.user_id = "test_user"
        self.assertEqual(self.place.user_id, "test_user")

    def test_name(self):
        self.assertIsNone(self.place.name)
        self.place.name = "test_name"
        self.assertEqual(self.place.name, "test_name")


if __name__ == '__main__':
    unittest.main()
