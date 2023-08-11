#!/usr/bin/python3
"""
test_base_model module
"""
from unittest import TestCase
from uuid import uuid4
from datetime import datetime
from time import sleep
import pycodestyle
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    """
    Test cases for the BaseModel class
    """

    def test_pep(self):
        """test pep"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py',
                                    'tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__("models.base_model").__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_init_doc(self):
        """test init method documentation"""
        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_str_doc(self):
        """test str functiom documentation"""
        doc = BaseModel.__str__.__doc__
        self.assertGreater(len(doc), 1)

    def test_save_doc(self):
        """test save method documentation"""
        doc = BaseModel.save.__doc__
        self.assertGreater(len(doc), 1)

    def test_to_dict_doc(self):
        """test to_dict method documentation"""
        doc = BaseModel.to_dict.__doc__
        self.assertGreater(len(doc), 1)

    def test_init(self):
        """test init method"""
        obj = BaseModel()

        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIsInstance(obj.created_at, datetime)

    def test_save(self):
        """test save method"""
        obj = BaseModel()
        sleep(1)

        now = datetime.now().replace(microsecond=0)
        obj.save()
        self.assertEqual(obj.updated_at.replace(microsecond=0), now)

    def test_to_dict(self):
        """test to_dict method"""
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 89

        output = obj.to_dict()

        self.assertIsInstance(output, dict)

        o_id = output['id']
        updated_at = output['updated_at']
        created_at = output['created_at']
        class_name = output['__class__']
        name = output['name']
        my_number = output['my_number']

        self.assertIsInstance(o_id, str)
        self.assertIsInstance(updated_at, str)
        self.assertIsInstance(created_at, str)
        self.assertIsInstance(class_name, str)
        self.assertIsInstance(name, str)
        self.assertIsInstance(my_number, int)
