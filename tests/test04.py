#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '05 December 2023'
__version__ = '0.1.0'

import unittest
from lib import day04


class TestDay04(unittest.TestCase):
    def test_day_04_part_1_short(self):
        self.assertEqual(day04.day_04_part_1(day04.get_input_data('inputs/input_04_short.txt')), 13)

    def test_day_04_part_1_full(self):
        self.assertEqual(day04.day_04_part_1(day04.get_input_data('inputs/input_04.txt')), 27845)
    

if __name__ == '__main__':
    unittest.main()
