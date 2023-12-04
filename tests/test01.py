#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '01 December 2023'
__version__ = '0.1.0'

import unittest
from day01 import *


class TestDay01(unittest.TestCase):

    def test_get_digits_part_2_01(self):
        self.assertEqual(get_digits_part_2('one'), ['1'])

    def test_get_digits_part_2_02(self):
        self.assertEqual(get_digits_part_2('twone'), ['2', '1'])

    def test_get_digits_part_2_03(self):
        self.assertEqual(get_digits_part_2('two1nine'), ['2', '1', '9'])

    def test_get_digits_part_2_04(self):
        self.assertEqual(get_digits_part_2('abcone2threexyz'), ['1', '2', '3'])

    def test_get_digits_part_2_05(self):
        self.assertEqual(get_digits_part_2('zoneight234'), ['1', '8', '2', '3', '4'])


if __name__ == '__main__':
    unittest.main()
