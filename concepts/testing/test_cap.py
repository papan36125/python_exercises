"""
A simple unit test script for cap.py
"""

import unittest
import cap

class TestCap(unittest.TestCase):
    """
    Class that test cap.py
    """
    def test_one_word(self):
        """
        Unit test function to test one worded string against function in cap.py
        """
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        """
        Unit test function to test multiple worded string against function in cap.py
        """
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

# Run unit test
if __name__ == '__main__':
    unittest.main()
