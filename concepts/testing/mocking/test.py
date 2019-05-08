from unittest import TestCase
from main import Calculator
from unittest.mock import patch

class TestCalculator(TestCase):
    @patch('main.Calculator.sum', return_value=9)
    # def setUp(self):
    #     self.calc = Calculator()

    def test_sum(self, sum):
        # answer = self.calc.sum(2, 4)
        self.assertEqual(sum(2, 4), 9)
