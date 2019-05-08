from unittest.mock import patch
from main import HelloTest
import unittest

class TestFoo(unittest.TestCase):

    @patch('main.HelloTest.bar')
    def test_foo_case(self, mock_bar):

        ht = HelloTest()

        ht.foo("some string")
        self.assertEqual(ht.msg, "SOME STRING")
        self.assertTrue(mock_bar.called)
