#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '06 December 2023'
__version__ = '0.1.0'


def get_input_data(filename: str) -> list:
    with open(filename, 'r') as my_file:
        puzzle_input = my_file.read()
    puzzle_input = [x.strip() for x in puzzle_input.strip().split('\n')]
    return puzzle_input


def day_05_part_1(puzzle_input: list) -> int:
    pass


def main() -> None:
    puzzle_input = get_input_data("inputs/input_05.txt")
    part_1 = day_05_part_1(puzzle_input=puzzle_input)
    print(f"The lowest location number that corresponds to any of the initial seed numbers is {part_1}.")


if __name__ == '__main__':
    main()
