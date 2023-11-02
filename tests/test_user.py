import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_instance(self):
        """Test if a User instance can be created"""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_default_values(self):
        """Test if the default values of the User attributes are empty strings"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attribute_assignment(self):
        """Test if the ser attributes ca be assigned"""
        user = User()
        user.email = "user@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        
        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()
