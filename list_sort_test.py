import unittest

from list_sort import list_sort


class listsortTest(unittest.TestCase):

    def test_integer_input(self):
        self.assertEqual(list_sort(5), {'evens': [], 'odds': [5], 'chars': []})

    def test_string_input(self):
        self.assertEqual(list_sort('string'),  {'evens': [], 'odds': [], 'chars': ['a', 'z']})

    def test_empty_list(self):
        self.assertEqual(list_sort([]), {'evens': [], 'odds': [], 'chars': []})

    def test_no_string(self):
        self.assertEqual(
            list_sort([2, 0, 5]),
            {'evens': [2, 0], 'odds': [5], 'chars': []}
            )

    def test_no_even(self):
        self.assertEqual(
            list_sort([7, 5, 1, 'a', 'z']),
            {'evens': [], 'odds': [1, 5, 7], 'chars': ['a', 'z']}
            )

    def test_no_odd(self):
        self.assertEqual(
            list_sort([2, 0, 6, 'a', 'z']),
            {'evens': [2, 0, 6], 'odds': [], 'chars': ['a', 'z']}
            )

    def test_complete_list(self):
        self.assertEqual(
            list_sort([2, 0, 6, 5, 1, 7, 'a', 'z']),
            {'evens': [0, 2, 6], 'odds': [1, 5, 7], 'chars': ['a', 'z']}
            )
