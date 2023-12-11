#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '10 December 2023'
__version__ = '0.2.0'

import unittest
from lib import day06


class TestDay06(unittest.TestCase):
    def test_parse_maps_01(self):
        self.assertEqual(True, True)

    def test_day_06_part_1_short(self):
        self.assertEqual(day06.day_06_part_1(day06.get_input_data('inputs/input_06_short.txt')), 288)

    def test_day_06_part_1_full(self):
        self.assertEqual(day06.day_06_part_1(day06.get_input_data('inputs/input_06.txt')), 131376)

    def test_day_06_part_2_short(self):
        self.assertEqual(day06.day_06_part_2(day06.get_input_data('inputs/input_06_short.txt')), 71503)

    def test_day_06_part_2_full(self):
        self.assertEqual(day06.day_06_part_2(day06.get_input_data('inputs/input_06.txt')), 34123437)


if __name__ == '__main__':
    unittest.main()
