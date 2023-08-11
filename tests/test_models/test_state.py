#!/usr/bin/python3
"""
test_state module
"""
from unittest import TestCase
import pycodestyle
from models.state import State


class TestState(TestCase):
    """
    TestState class
    """

    def test_pep(self):
        """test pep"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py',
                                    'tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.state').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = State.__doc__
        self.assertGreater(len(doc), 1)
