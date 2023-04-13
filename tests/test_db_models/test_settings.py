#!/usr/bin/python3
""" tests for class Setting"""

import unittest
from models.settings import Settings

class TestSettings(unittest.TestCase):
    """Test cases for the Settings class"""

    def setUp(self):
        """Set up test fixtures"""
        self.settings = Settings()

    def test_instance_creation(self):
        """Test that an instance of the Settings class is created"""
        self.assertIsInstance(self.settings, Settings)

    def test_user_id(self):
        """Test the user_id field"""
        self.assertIsNone(self.settings.user_id)
        self.settings.user_id = "123"
        self.assertEqual(self.settings.user_id, "123")

    def test_theme(self):
        """Test the theme field"""
        self.assertIsNone(self.settings.theme)
        self.settings.theme = "dark"
        self.assertEqual(self.settings.theme, "dark")

    def test_language(self):
        """Test the language field"""
        self.assertIsNone(self.settings.language)
        self.settings.language = "en"
        self.assertEqual(self.settings.language, "en")

    def test_notifications(self):
        """Test the notifications field"""
        self.assertIsNone(self.settings.notifications)
        self.settings.notifications = 1
        self.assertEqual(self.settings.notifications, 1)

if __name__ == '__main__':
    unittest.main()
