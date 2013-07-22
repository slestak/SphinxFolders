#coding=utf-8
u'''
Sample test module corresponding to the :mod:`sphinxfolders.code` module.
'''
import unittest
from sphinxfolders.code import sample_function

class SampleTest(unittest.TestCase):
    u'''Base test cases for the sample function provided in
    :func:`sphinxfolders.code.sample_function`.'''

    def test_1(self):
        u'''Test the sample_function with two arguments.'''
        self.assertEqual(sample_function(4, 4), 8)

    def test_2(self):
        u'''Test the sample_function with a single argument.'''
        self.assertEqual(sample_function(4), 8)

if __name__ == '__main__':
    unittest.main()