#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '11 December 2023'
__version__ = '0.1.0'

import unittest
from lib import day08


class TestDay08(unittest.TestCase):    
    def test_day_08_part_1_short(self):
        self.assertEqual(day08.day_08_part_1(day08.get_input_data('inputs/input_08_short.txt')), 6)

    def test_day_08_part_1_full(self):
        self.assertEqual(day08.day_08_part_1(day08.get_input_data('inputs/input_08.txt')), 13207)    


if __name__ == '__main__':
    unittest.main()
