#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '02 December 2023'
__version__ = '0.2.0'

import unittest
from day02 import *


class TestDay02(unittest.TestCase):

    def test_parse_games_01(self):
        self.assertEqual(parse_games(get_input_data('../inputs/input_02_short.txt')), 
                         [[1, {'red':  4, 'green':  2, 'blue':  6}],
                          [2, {'red':  1, 'green':  3, 'blue':  4}],
                          [3, {'red': 20, 'green': 13, 'blue':  6}],
                          [4, {'red': 14, 'green':  3, 'blue': 15}],
                          [5, {'red':  6, 'green':  3, 'blue':  2}],
                          ])
    
    def test_day_02_part_1_short(self):
        self.assertEqual(day_02_part_1(get_input_data('../inputs/input_02_short.txt')), 8)

    def test_day_02_part_1_full(self):
        self.assertEqual(day_02_part_1(get_input_data('../inputs/input_02.txt')), 2439)

    def test_day_02_part_2_short(self):
        self.assertEqual(day_02_part_2(get_input_data('../inputs/input_02_short.txt')), 2286)

    def test_day_02_part_2_full(self):
        self.assertEqual(day_02_part_2(get_input_data('../inputs/input_02.txt')), 63711)


if __name__ == '__main__':
    unittest.main()
