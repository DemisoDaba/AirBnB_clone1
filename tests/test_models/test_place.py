#!/usr/bin/python3
"""
test_place module
"""
from unittest import TestCase
import pycodestyle
from models.place import Place


class TestPlace(TestCase):
    """
    TestPlace class
    """

    def test_pep(self):
        """test pep"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py',
                                    'tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.place').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = Place.__doc__
        self.assertGreater(len(doc), 1)
