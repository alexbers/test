import unittest
import sufpref



class TestAll(unittest.TestCase):
    words = ['a', 'ab', 'abab', 'ababab', 'bababa', 'abcbca', 'abababa']

    def test_bf(self):
        arr, length = sufpref.solve_bf(self.words)
        self.assertEqual(length, 6)
        self.assertEqual(arr[1], 'abababa')

    def test_hash(self):
        arr, length = sufpref.solve_hash(self.words)
        self.assertEqual(length, 6)
        self.assertEqual(arr[1], 'abababa')
