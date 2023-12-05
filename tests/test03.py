#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '05 December 2023'
__version__ = '0.2.1'

import unittest
from lib import day03


class TestDay03(unittest.TestCase):
    def test_get_symbol_locations_01(self):
        self.assertEqual(day03.get_symbol_locations(day03.get_input_data('inputs/input_03_short.txt')),
                         [(3, 1), (6, 3), (3, 4), (5, 5), (3, 8), (5, 8)])
        
    def test_get_neighbors_01(self):
        known_neighbors = [(-1, 0),
                          (1, 0),
                          (-1, -1),
                          (-1, 1),
                          (1, -1),
                          (1, 1),
                          (0, -1),
                          (0, 1)]
        test_neighbors = day03.get_neighbors(0, 0)
        for each in test_neighbors:
            if each not in known_neighbors:
                self.assetTrue(False)
        self.assertTrue(len(known_neighbors) == len(test_neighbors))

    def test_day_03_part_1_short(self):
        self.assertEqual(day03.day_03_part_1(day03.get_input_data('inputs/input_03_short.txt')), 4361)

    def test_day_03_part_1_full(self):
        self.assertEqual(day03.day_03_part_1(day03.get_input_data('inputs/input_03.txt')), 525181)
    
    def test_day_03_part_2_short(self):
        self.assertEqual(day03.day_03_part_2(day03.get_input_data('inputs/input_03_short.txt')), 467835)

    def test_day_03_part_2_full(self):
        self.assertEqual(day03.day_03_part_2(day03.get_input_data('inputs/input_03.txt')), 84289137)


if __name__ == '__main__':
    unittest.main()
