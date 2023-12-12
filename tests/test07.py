#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '11 December 2023'
__version__ = '0.1.0'

import unittest
from lib import day07


class TestDay07(unittest.TestCase):
    def test_sort_hands_01(self):
        hands_bids = day07.parse_hands(day07.get_input_data('inputs/input_07_short.txt'))[0:2]
        self.assertEqual(day07.sort_hands(hands_bids), [('T55J5', '684'), ('32T3K', '765')])
    
    def test_sort_hands_02(self):
        hands_bids = day07.parse_hands(day07.get_input_data('inputs/input_07_short.txt'))
        self.assertEqual(day07.sort_hands(hands_bids), [('QQQJA', '483'), ('T55J5', '684'), ('KK677', '28'), ('KTJJT', '220'), ('32T3K', '765')])

    def test_sort_hands_2_01(self):
        hands_bids = day07.parse_hands(day07.get_input_data('inputs/input_07_short.txt'))
        self.assertEqual(day07.sort_hands_2(hands_bids), [('KTJJT', '220'), ('QQQJA', '483'), ('T55J5', '684'), ('KK677', '28'), ('32T3K', '765')])

    def test_get_hand_type_01(self):
        self.assertEqual(day07.get_hand_type('KK677'), 'Two pair')
    
    def test_get_hand_type_02(self):
        self.assertEqual(day07.get_hand_type('32T3K'), 'One pair')
    
    def test_get_hand_type_03(self):
        self.assertEqual(day07.get_hand_type('23456'), 'High card')
    
    def get_hand_type_2_01(self):
        self.assertEqual(day07.get_hand_type('KK677'), 'Two pair')
    
    def get_hand_type_2_02(self):
        self.assertEqual(day07.get_hand_type('QJJQ2'), 'Four of a kind')
    
    def get_hand_type_2_03(self):
        self.assertEqual(day07.get_hand_type('KTJJT'), 'Four of a kind')

    def get_hand_type_2_04(self):
        self.assertEqual(day07.get_hand_type('QQQJA'), 'Four of a kind')

    def get_hand_type_2_05(self):
        self.assertEqual(day07.get_hand_type('T55J5'), 'Four of a kind')
    
    def get_hand_type_2_06(self):
        self.assertEqual(day07.get_hand_type('2332J'), 'Full house')
    
    def get_hand_type_2_07(self):
        self.assertEqual(day07.get_hand_type('32T3K'), 'One pair')
    
    def test_hand_greater_than_or_equal_2_01(self):
        self.assertFalse(day07.hand_greater_than_or_equal_2('QQQJA', 'KTJJT'))
    
    def test_hand_greater_than_or_equal_2_02(self):
        self.assertTrue(day07.hand_greater_than_or_equal_2('KTJJT', 'QQQJA'))
    
    def test_day_07_part_1_short(self):
        self.assertEqual(day07.day_07_part_1(day07.get_input_data('inputs/input_07_short.txt')), 6440)

    def test_day_07_part_1_full(self):
        self.assertEqual(day07.day_07_part_1(day07.get_input_data('inputs/input_07.txt')), 250347426)
    
    def test_day_07_part_2_short(self):
        self.assertEqual(day07.day_07_part_2(day07.get_input_data('inputs/input_07_short.txt')), 5905)

    def test_day_07_part_2_full(self):
        self.assertEqual(day07.day_07_part_2(day07.get_input_data('inputs/input_07.txt')), 251224870)


if __name__ == '__main__':
    unittest.main()
