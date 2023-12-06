#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '06 December 2023'
__version__ = '0.1.0'

import unittest
from lib import day05


class TestDay05(unittest.TestCase):
    def test_parse_maps_01(self):
        self.assertEqual(True, True)

    def test_day_05_part_1_short(self):
        self.assertEqual(day05.day_05_part_1(day05.get_input_data('inputs/input_05_short.txt')), 35)

    def test_day_05_part_1_full(self):
        self.assertEqual(day05.day_05_part_1(day05.get_input_data('inputs/input_05.txt')), 261668924)
    
    def test_day_05_part_2_short(self):
        self.assertEqual(day05.day_05_part_2(day05.get_input_data('inputs/input_05_short.txt')), 0)

    def test_day_05_part_2_full(self):
        self.assertEqual(day05.day_05_part_2(day05.get_input_data('inputs/input_05.txt')), 0)
    

if __name__ == '__main__':
    unittest.main()
