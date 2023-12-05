#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '01 December 2023'
__version__ = '0.1.1'

import unittest
from lib import day03


class TestDay03(unittest.TestCase):
    def test_get_all_locations(self):
        self.assertEqual(day03.get_all_locations(day03.get_input_data('../inputs/input_03_short.txt')),
                         {(0, 0): '467',
                          (1, 0): '467',
                          (2, 0): '467',
                          (5, 0): '114',
                          (6, 0): '114',
                          (7, 0): '114',
                          (2, 2): '35',
                          (3, 2): '35',
                          (6, 2): '633',
                          (7, 2): '633',
                          (8, 2): '633',
                          (0, 4): '617',
                          (1, 4): '617',
                          (2, 4): '617',
                          (7, 5): '58',
                          (8, 5): '58',
                          (2, 6): '592',
                          (3, 6): '592',
                          (4, 6): '592',
                          (6, 7): '755',
                          (7, 7): '755',
                          (8, 7): '755',
                          (1, 9): '664',
                          (2, 9): '664',
                          (3, 9): '664',
                          (5, 9): '598',
                          (6, 9): '598',
                          (7, 9): '598',
                          })
        
    def test_get_neighbors_01(self):
        self.assertEqual(day03.get_neighbors(0, 0),
                         [(-1, 0),
                          (1, 0),
                          (-1, -1),
                          (-1, 1),
                          (1, -1),
                          (1, 1),
                          (0, -1),
                          (0, 1)])

    def test_day_03_part_1_short(self):
        self.assertEqual(day03.day_03_part_1(day03.get_input_data('inputs/input_03_short.txt')), 4361)

    def test_day_03_part_1_full(self):
        self.assertEqual(day03.day_03_part_1(day03.get_input_data('inputs/input_03.txt')), 0)


if __name__ == '__main__':
    unittest.main()
