"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
from unittest.mock import patch


def test_read_numbers_without_text_input():
    ...


def test_read_numbers_with_text_input():
    ...


######
import unittest
from unittest.mock import patch

# Your function to test
def read_numbers():
    raw = input("Enter numbers separated by commas: ")
    try:
        return [int(x.strip()) for x in raw.split(',')]
    except ValueError:
        raise ValueError("All inputs must be integers.")

class TestReadNumbers(unittest.TestCase):

    @patch('builtins.input', return_value='1, 2, 3, 4')
    def test_valid_input(self, mock_input):
        result = read_numbers()
        self.assertEqual(result, [1, 2, 3, 4])

    @patch('builtins.input', return_value='1, 2, Text')
    def test_invalid_input(self, mock_input):
        with self.assertRaises(ValueError) as context:
            read_numbers()
        self.assertEqual(str(context.exception), "All inputs must be integers.")

if __name__ == '__main__':
    unittest.main()
