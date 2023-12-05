#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '03 December 2023'
__version__ = '0.1.3'

import re


def get_input_data(filename: str) -> list:
    with open(filename, 'r') as my_file:
        puzzle_input = my_file.read()
    puzzle_input = [x.strip() for x in puzzle_input.strip().split('\n')]
    return puzzle_input


def get_unique_symbols(puzzle_input: list) -> list:
    result = list()
    for each_line in puzzle_input:
        s = each_line.replace('.', '')
        for x in range(0, 10):
            s = s.replace(str(x), '')
        s = list(set([y for y in s]))
        result += s
    result = list(set(result))
    return result


def get_all_locations(puzzle_input) -> dict:
    y = 0
    locations = dict()
    for each_line in puzzle_input:
        for each_number in re.finditer("[0-9]+", each_line):
            for x in range(each_number.start(), each_number.end()):
                locations[(x, y)] = each_number[0]
        y += 1
    return locations


def get_neighbors(x: int, y: int) -> list:
    return [(x-1, y),
            (x-1, y-1),
            (x-1, y+1),
            (x, y-1),
            (x, y+1),
            (x+1, y),
            (x+1, y-1),
            (x+1, y+1)]


def get_symbol_locations(puzzle_input: list) -> list:
    y = 0
    non_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    symbol_locations = list()
    for each_line in puzzle_input:
        for x in range(0, len(each_line)):
            if each_line[x] not in non_symbols:
                symbol_locations.append((x, y))
        y += 1
    return symbol_locations


def day_03_part_1(puzzle_input: list) -> int:
    part_numbers = list()
    locations = get_all_locations(puzzle_input=puzzle_input)
    for x, y in get_symbol_locations(puzzle_input=puzzle_input):
        for each_neighbor in get_neighbors(x, y):
            if each_neighbor in locations.keys():
                part_numbers.append(int(locations[each_neighbor]))
    part_numbers = list(set(part_numbers))
    return sum(part_numbers)


def main() -> None:
    puzzle_input = get_input_data("inputs/input_03.txt")
    part_1 = day_03_part_1(puzzle_input=puzzle_input)
    print(f"The sum of all the part numbers in the engine schematic is {part_1}")


if __name__ == '__main__':
    main()
