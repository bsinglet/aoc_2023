#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '02 December 2023'
__version__ = '0.1.0'

import unittest
from day02 import *

class TestDay02(unittest.TestCase):

    def test_parse_games_01(self):
        self.assertEqual(parse_games(get_input_data('input_02_short.txt')), 
                         [[1, {'red':  4, 'green':  2, 'blue':  6}],
                          [2, {'red':  1, 'green':  3, 'blue':  4}],
                          [3, {'red': 20, 'green': 13, 'blue':  6}],
                          [4, {'red': 14, 'green':  3, 'blue': 15}],
                          [5, {'red':  6, 'green':  3, 'blue':  2}],
                          ])


if __name__ == '__main__':
    unittest.main()
