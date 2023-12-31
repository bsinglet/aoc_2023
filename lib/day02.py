#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '02 December 2023'
__version__ = '0.2.0'


def get_input_data(filename: str) -> list:
    with open(filename, 'r') as my_file:
        puzzle_input = my_file.read()
    puzzle_input = [x.strip() for x in puzzle_input.strip().split('\n')]
    return puzzle_input


def parse_games(puzzle_input: list) -> list:
    parsed_games = list()
    for each_game in puzzle_input:
        game_id = int(each_game.split(':')[0].split(' ')[-1])
        max_each = {'red': 0, 'green': 0, 'blue': 0}
        for each_round in each_game.split(':')[1].strip().split(';'):
            for each_color in each_round.split(','):
                number, color = each_color.strip().split(' ')
                if color not in max_each.keys():
                    RuntimeError(f"Did not recognize color {color}")
                max_each[color] = max(max_each[color], int(number))
        parsed_games.append([game_id, max_each])
    return parsed_games


def day_02_part_1(puzzle_input: list) -> int:
    parsed_games = parse_games(puzzle_input)
    possible_games = 0
    for each_game in parsed_games:
        if each_game[1]['red'] > 12 or each_game[1]['green'] > 13 or each_game[1]['blue'] > 14:
            continue
        possible_games += each_game[0]
    return possible_games


def day_02_part_2(puzzle_input: list) -> int:
    parsed_games = parse_games(puzzle_input)
    power_sum = 0
    for each_game in parsed_games:
        power_sum += each_game[1]['red'] * each_game[1]['green'] * each_game[1]['blue']
    return power_sum


def main() -> None:
    puzzle_input = get_input_data("inputs/input_02.txt")
    part_1 = day_02_part_1(puzzle_input=puzzle_input)
    print(f"The sum of the IDs of the possible games is {part_1}")
    part_2 = day_02_part_2(puzzle_input=puzzle_input)
    print(f"The sum of the power of these sets is {part_2}")


if __name__ == '__main__':
    main()
