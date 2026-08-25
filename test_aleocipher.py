# test_aleocipher.py
"""
Tests for AleoCipher module.
"""

import unittest
from aleocipher import AleoCipher

class TestAleoCipher(unittest.TestCase):
    """Test cases for AleoCipher class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AleoCipher()
        self.assertIsInstance(instance, AleoCipher)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AleoCipher()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
