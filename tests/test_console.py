#!/usr/bin/python3

import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
""" Test cases class """

    def test_prompt(self):
        """ Test prompt """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


if __name__ == '__main__':
    unittest.main()
