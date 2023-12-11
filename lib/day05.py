#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '06 December 2023'
__version__ = '0.2.3'

from tqdm import tqdm


def get_input_data(filename: str) -> list:
    with open(filename, 'r') as my_file:
        puzzle_input = my_file.read()
    puzzle_input = [x.strip() for x in puzzle_input.strip().split('\n')]
    return puzzle_input


def parse_maps(puzzle_input: list) -> list:
    my_maps = list()
    my_maps.append([int(x) for x in puzzle_input[0].split(':')[1].strip().split(' ')])
    line_number = 2
    while line_number < len(puzzle_input):
        if puzzle_input[line_number].strip() == '':
            line_number += 1
            continue
        map_name = puzzle_input[line_number].strip(':')[0].strip()
        map_lines = list()
        line_number += 1
        while line_number < len(puzzle_input) and puzzle_input[line_number].strip() != '':
            map_lines.append([int(x) for x in puzzle_input[line_number].strip().split(' ')])
            line_number += 1
        my_maps.append(map_lines)
    return my_maps


def find_in_map(current_id: int, each_map: list) -> int:
    # if this isn't in the map, then it stays the same
    matching_id = current_id
    for each_line in each_map:
        if current_id >= each_line[1] and current_id < each_line[1] + each_line[2]:
            matching_id += each_line[0] - each_line[1]
            break
    return matching_id


def find_in_map_2(current_id: int, each_map: list) -> int:
    # if this isn't in the map, then it stays the same
    matching_id = current_id
    for each_line in each_map:
        if current_id in range(each_line[0], each_line[0] + each_line[2]):
            matching_id += each_line[1] - each_line[0]
            break
    return matching_id


def is_in_seed_range(current_id: int, seed_ranges: list) -> bool:
    for each_range in seed_ranges:
        # print(f"Checking {current_id} against {each_range}")
        if current_id in range(each_range[0], each_range[1]):
            return True
    return False


def day_05_part_1(puzzle_input: list) -> int:
    parsed_maps = parse_maps(puzzle_input=puzzle_input)
    seed_to_location = dict()
    for each_seed in parsed_maps[0]:
        current_id = each_seed
        for map_id in range(1, len(parsed_maps)):
            current_id = find_in_map(current_id, parsed_maps[map_id])
        seed_to_location[each_seed] = current_id
    return min(seed_to_location.values())


def day_05_part_2(puzzle_input: list) -> int:
    parsed_maps = parse_maps(puzzle_input=puzzle_input)
    seed_ranges = list()
    for index in range(0, len(parsed_maps[0]), 2):
        seed_ranges.append((parsed_maps[0][index], parsed_maps[0][index] + parsed_maps[0][index + 1]))
    parsed_maps = parsed_maps[1:]
    parsed_maps.reverse()
    for each_location in tqdm(range(0, 25_000_000)):
        current_id = each_location
        for map_id in range(len(parsed_maps)):
            current_id = find_in_map_2(current_id, parsed_maps[map_id])
        if is_in_seed_range(current_id, seed_ranges):
            return each_location
    return None


def main() -> None:
    puzzle_input = get_input_data("inputs/input_05.txt")
    part_1 = day_05_part_1(puzzle_input=puzzle_input)
    print(f"The lowest location number that corresponds to any of the initial seed numbers is {part_1}.")
    part_2 = day_05_part_2(puzzle_input=puzzle_input)
    print(f"The REAL (part 2) lowest location number that corresponds to any of the initial seed numbers is {part_2}.")


if __name__ == '__main__':
    main()
