#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '05 December 2023'
__version__ = '0.2.0'

import math


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


def parse_cards_2(puzzle_input: list) -> list:
    result = list()
    for each_line in puzzle_input:
        # remove any double and triple spaces, luckily there are no higher
        each_line = each_line.replace('   ', ' ')
        each_line = each_line.replace('  ', ' ')
        card_number = int(each_line.split(':')[0].strip().split(' ')[1].strip())
        each_line = each_line.split(':')[1].strip()
        first, second = each_line.split('|')
        first = [int(x) for x in first.strip().split(' ')]
        second = [int(x) for x in second.strip().split(' ')]
        result.append((card_number, first, second))
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


def day_04_part_2(puzzle_input: list) -> int:
    held_scratchcards = dict()
    won_scratchcards = dict()
    parsed_cards = parse_cards_2(puzzle_input)
    # initialize the cards you start with
    held_scratchcards = {x[0]: 1 for x in parsed_cards}
    # score the cards
    for card_num, first, second in parsed_cards:
        num_matched = 0
        for each_number in second:
            if each_number in first:
                # this is a match
                num_matched += 1
        if num_matched > 0:
            won_scratchcards[card_num] = held_scratchcards[card_num]
            for each_win in range(num_matched):
                held_scratchcards[card_num + each_win + 1] += held_scratchcards[card_num]
        else:
            won_scratchcards[card_num] = held_scratchcards[card_num]
    return sum(won_scratchcards.values())


def main() -> None:
    puzzle_input = get_input_data("inputs/input_04.txt")
    part_1 = day_04_part_1(puzzle_input=puzzle_input)
    print(f"The cards are worth {part_1} points in total.")
    part_2 = day_04_part_2(puzzle_input=puzzle_input)
    print(f"You end up with a total of {part_2} scratchcards.")


if __name__ == '__main__':
    main()
