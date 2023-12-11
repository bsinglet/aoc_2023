#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '10 December 2023'
__version__ = '0.1.0'

import re


def get_input_data(filename: str) -> list:
    with open(filename, 'r') as my_file:
        puzzle_input = my_file.read()
    puzzle_input = [x.strip() for x in puzzle_input.strip().split('\n')]
    return puzzle_input

def parse_input(puzzle_input: list) -> list:
    times = list()
    distances = list()
    for each_time in re.finditer('\d+', puzzle_input[0]):
        times.append(int(each_time[0]))
    for each_distance in re.finditer('\d+', puzzle_input[1]):
        distances.append(int(each_distance[0]))
    return zip(times, distances)


def generate_wins(time: int, record_distance: int) -> int:
    wins = 0
    for speed in range(1, time):
        distance = (time - speed) * speed
        if distance > record_distance:
            wins += 1
    return wins


def day_06_part_1(puzzle_input: list) -> int:
    ways_to_beat = 1
    time_distances = parse_input(puzzle_input)
    for time, record_distance in time_distances:
        ways_to_beat *= generate_wins(time, record_distance)
    return ways_to_beat    


def main() -> None:
    puzzle_input = get_input_data("inputs/input_06.txt")
    part_1 = day_06_part_1(puzzle_input=puzzle_input)
    print(f"If you multiply these numbers together you get {part_1}.")


if __name__ == '__main__':
    main()
