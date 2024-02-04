#!/usr/bin/python3
"""
Unit tests for the State class.
"""
import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class."""

    def test_init(self):
        """Test initialization of State."""
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertEqual(state.name, "")

    def test_str(self):
        """Test string representation."""
        state = State()
        self.assertEqual(str(state), "[State] ({}) {}".format(state.id, state.__dict__))

    def test_to_dict(self):
        """Test to_dict method."""
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['id'], state.id)
        self.assertEqual(state_dict['created_at'], state.created_at.isoformat())
        self.assertEqual(state_dict['updated_at'], state.updated_at.isoformat())
        self.assertEqual(state_dict['name'], state.name)


if __name__ == '__main__':
    unittest.main()
