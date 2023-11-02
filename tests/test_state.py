import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_state_instance(self):
        """Test if a State instance can be created"""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_name_default(self):
        """Test if the 'name' attribute of a State instance is empty by default"""
        state = State()
        self.assertEqual(state.name, "")

    def test_state_name_assignment(self):
        """Test if the 'name' attribute can be assigned a value"""
        state = State()
        state.name = "New York"
        self.assertEqual(state.name, "New York")

if __name__ == '__main__':
    unittest.main()
