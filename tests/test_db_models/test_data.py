#!/usr/bin/python3
""" """

import unittest
from models.data import Data
from models.user import User

class TestDataModel(unittest.TestCase):
    def setUp(self):
        """Set up a user instance for testing"""
        self.user = User(email="mugabijoshgreen@gmail.com", password="password")

    def test_data_creation(self):
        """Test that a Data instance can be created"""
        data = Data(user_id=self.user.id, name="test_data", value="test_value")
        self.assertIsInstance(data, Data)

    def test_data_attributes(self):
        """Test that a Data instance has the expected attributes"""
        data = Data(user_id=self.user.id, name="test_data", value="test_value")
        self.assertEqual(data.user_id, self.user.id)
        self.assertEqual(data.name, "test_data")
        self.assertEqual(data.value, "test_value")

    def test_data_str_representation(self):
        """Test that a Data instance can be represented as a string"""
        data = Data(user_id=self.user.id, name="test_data", value="test_value")
        expected_str = f"<Data {data.id}: user_id={self.user.id}, name='test_data', value='test_value'>"
        self.assertEqual(str(data), expected_str)

    def test_data_save_to_db(self):
        """Test that a Data instance can be saved to the database"""
        data = Data(user_id=self.user.id, name="test_data", value="test_value")
        data.save()
        self.assertIsNotNone(data.id)

    def test_data_delete_from_db(self):
        """Test that a Data instance can be deleted from the database"""
        data = Data(user_id=self.user.id, name="test_data", value="test_value")
        data.save()
        data.delete()
        self.assertIsNone(Data.get(data.id))
