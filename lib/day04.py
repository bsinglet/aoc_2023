#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '05 December 2023'
__version__ = '0.1.0'

import math
import re


def get_input_data(filename: str) -> list:
    with open(filename, 'r') as my_file:
        puzzle_input = my_file.read()
    puzzle_input = [x.strip() for x in puzzle_input.strip().split('\n')]
    return puzzle_input


def parse_cards(puzzle_input: list) -> list:
    result = list()
    for each_line in puzzle_input:
        # remove any double spaces, luckily there are no triple or higher
        each_line = each_line.replace('  ', ' ')
        each_line = each_line.split(':')[1].strip()
        first, second = each_line.split('|')
        first = [int(x) for x in first.strip().split(' ')]
        second = [int(x) for x in second.strip().split(' ')]
        result.append((first, second))
    return result


def day_04_part_1(puzzle_input: list) -> int:
    points_sum = 0
    parsed_cards = parse_cards(puzzle_input)
    for first, second in parsed_cards:
        num_matched = 0
        for each_number in second:
            if each_number in first:
                # this is a match
                num_matched += 1
        if num_matched > 0:
            points_sum += int(math.pow(2, num_matched-1))
    return points_sum


def main() -> None:
    puzzle_input = get_input_data("inputs/input_04.txt")
    part_1 = day_04_part_1(puzzle_input=puzzle_input)
    print(f"The cards are worth {part_1} points in total.")


if __name__ == '__main__':
    main()
