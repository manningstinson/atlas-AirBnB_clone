import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    def test_attributes(self):
        """
        Test the attributes of User instance
        """
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_email_default_value(self):
        """
        Test the default value of email attribute
        """
        user = User()
        self.assertEqual(user.email, "")

    def test_password_default_value(self):
        """
        Test the default value of password attribute
        """
        user = User()
        self.assertEqual(user.password, "")

    def test_first_name_default_value(self):
        """
        Test the default value of first_name attribute
        """
        user = User()
        self.assertEqual(user.first_name, "")

    def test_last_name_default_value(self):
        """
        Test the default value of last_name attribute
        """
        user = User()
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
