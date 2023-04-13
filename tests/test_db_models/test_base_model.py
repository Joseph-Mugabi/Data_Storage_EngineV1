#!/usr/bin/python3
"""test BaseModel for ways it behave and documentation"""
from datetime import datetime
import inspect
import models
import pep8 as pycodestyle
import time
import unittest
from unittest import mock
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Tests for documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/base_model.py conforms to PEP8."""
        for path in ['models/base_model.py',
                     'tests/test_db_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    def test_instantiation(self):
        """Test that object is correctly created"""
        instce = BaseModel()
        self.assertIs(type(instce), BaseModel)
        instce.name = "ALX"
        instce.number = 89
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, instce.__dict__)
                self.assertIs(type(instce.__dict__[attr]), typ)
        self.assertEqual(instce.name, "ALX")
        self.assertEqual(instce.number, 89)

    def test_datetime_attributes(self):
        """Test that two BaseModel instances have different datetime objects
        and that upon creation have identical updated_at and created_at
        value."""
        tic = datetime.now()
        instce1 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= instce1.created_at <= toc)
        time.sleep(1e-4)
        tic = datetime.now()
        instce2 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= instce2.created_at <= toc)
        self.assertEqual(instce1.created_at, instce1.updated_at)
        self.assertEqual(instce2.created_at, instce2.updated_at)
        self.assertNotEqual(instce1.created_at, instce2.created_at)
        self.assertNotEqual(instce1.updated_at, instce2.updated_at)

    def test_uuid(self):
        """Test that id is a valid uuid"""
        instce1 = BaseModel()
        instce2 = BaseModel()
        for instce in [instce1, instce2]:
            uuid = instce.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(instce1.id, instce2.id)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "ALX")
        self.assertEqual(d['my_number'], 89)

    def test_to_dict_values(self):
        """test for values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        base_model = BaseModel()
        new_dict = base_model.to_dict()
        self.assertEqual(new_dict["__class__"], "BaseModel")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         base_model.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         base_model.updated_at.strftime(t_format))

    def test_str(self):
        """test for the str method has the correct output"""
        instce = BaseModel()
        string = "[BaseModel] ({}) {}".format(instce.id, instce.__dict__)
        self.assertEqual(string, str(instce))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        instce = BaseModel()
        old_created_at = instce.created_at
        old_updated_at = instce.updated_at
        instce.save()
        new_created_at = instce.created_at
        new_updated_at = instce.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)
