#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '01 December 2023'
__version__ = '0.2.0'

import unittest
from lib import day01


class TestDay01(unittest.TestCase):

    def test_get_digits_part_2_01(self):
        self.assertEqual(day01.get_digits_part_2('one'), ['1'])

    def test_get_digits_part_2_02(self):
        self.assertEqual(day01.get_digits_part_2('twone'), ['2', '1'])

    def test_get_digits_part_2_03(self):
        self.assertEqual(day01.get_digits_part_2('two1nine'), ['2', '1', '9'])

    def test_get_digits_part_2_04(self):
        self.assertEqual(day01.get_digits_part_2('abcone2threexyz'), ['1', '2', '3'])

    def test_get_digits_part_2_05(self):
        self.assertEqual(day01.get_digits_part_2('zoneight234'), ['1', '8', '2', '3', '4'])
    
    def test_day_01_part_1_short(self):
        self.assertEqual(day01.day_01_part_1(day01.get_input_data('inputs/input_01_short_a.txt')), 142)

    def test_day_01_part_1_full(self):
        self.assertEqual(day01.day_01_part_1(day01.get_input_data('inputs/input_01.txt')), 54605)
    
    def test_day_01_part_2_short(self):
        self.assertEqual(day01.day_01_part_2(day01.get_input_data('inputs/input_01_short_b.txt')), 281)
    
    def test_day_01_part_2_full(self):
        self.assertEqual(day01.day_01_part_2(day01.get_input_data('inputs/input_01.txt')), 55429)


if __name__ == '__main__':
    unittest.main()
