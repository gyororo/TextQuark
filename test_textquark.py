# test_textquark.py
"""
Tests for TextQuark module.
"""

import unittest
from textquark import TextQuark

class TestTextQuark(unittest.TestCase):
    """Test cases for TextQuark class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TextQuark()
        self.assertIsInstance(instance, TextQuark)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TextQuark()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
