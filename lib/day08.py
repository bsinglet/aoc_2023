#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '11 December 2023'
__version__ = '0.1.0'

from tqdm import tqdm


def get_input_data(filename: str) -> list:
    with open(filename, 'r') as my_file:
        puzzle_input = my_file.read()
    puzzle_input = [x.strip() for x in puzzle_input.strip().split('\n')]
    return puzzle_input



def parse_node_map(node_lines: list) -> dict:
    node_map = dict()
    for each_line in node_lines:
        start = each_line.split('=')[0].strip()
        left = each_line.split('(')[1].split(',')[0]
        right = each_line.split(',')[1].split(')')[0].strip()
        node_map[start] = (left, right)
    return node_map


def day_08_part_1(puzzle_input: list) -> int:
    traversal_order = [x for x in puzzle_input[0].strip()]
    node_map = parse_node_map(puzzle_input[2:])
    #print(node_map)
    steps_taken = 0
    position = 'AAA'
    while position != 'ZZZ':
        if traversal_order[steps_taken % len(traversal_order)] == 'L':
            position = node_map[position][0]
        else:
            position = node_map[position][1]
        steps_taken += 1
    return steps_taken


def main() -> None:
    puzzle_input = get_input_data("inputs/input_08.txt")
    part_1 = day_08_part_1(puzzle_input=puzzle_input)
    print(f"The number of steps it takes to reach ZZZ for part 1 are {part_1}.")



if __name__ == '__main__':
    main()
