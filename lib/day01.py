#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '01 December 2023'
__version__ = '0.2.0'


def get_input_data(filename: str) -> list:
    with open(filename, 'r') as my_file:
        puzzle_input = my_file.read()
    puzzle_input = [x.strip() for x in puzzle_input.strip().split('\n')]
    return puzzle_input


def isDigit(s: str) -> bool:
    if s >= '0' and s <= '9':
        return True
    return False


def isDigit_part_2(s: str) -> bool:
    if s in get_word_mappings().keys():
        return True
    return False


def get_word_mappings() -> list:
    return {'zero'  : '0',
            'one'   : '1',
            'two'   : '2',
            'three' : '3',
            'four'  : '4',
            'five'  : '5',
            'six'   : '6',
            'seven' : '7',
            'eight' : '8',
            'nine'  : '9'}


def get_digits_part_2(s: str) -> list():
    word_mappings = get_word_mappings()
    digits = list()
    start, end = (0, 3)
    while start < len(s):
        if isDigit(s[start]):
            digits.append(s[start])
            start += 1
            end = start + 3
        elif s[start:end] in word_mappings.keys():
            digits.append(word_mappings[s[start:end]])
            start += 1
            end = start + 3
        elif end - start >= 5:
            start += 1
            end = start + 3
        else:
            end += 1
    return digits


def day_01_part_1(puzzle_input: list) -> int:
    calibration_sum = 0
    for each_line in puzzle_input:
        digits = filter(isDigit, [x for x in each_line])
        digits = [x for x in digits]
        if len(digits) == 0:
            continue
        try:
            calibration_sum += int(digits[0] + digits[-1])
        except:
            print(f"Failed 1 on line {each_line} with digits {digits}")
    return calibration_sum


def day_01_part_2(puzzle_input: list) -> int:
    calibration_sum = 0
    for each_line in puzzle_input:
        digits = get_digits_part_2(each_line)
        try:
            calibration_sum += int(digits[0] + digits[-1])
        except:
            print(f"Failed on line {each_line} with digits {digits}")
    return calibration_sum


def main() -> None:
    puzzle_input = get_input_data("inputs/input_01.txt")
    part_1 = day_01_part_1(puzzle_input=puzzle_input)
    print(f"The sum of all calibration values is {part_1}")
    part_2 = day_01_part_2(puzzle_input=puzzle_input)
    print(f"The REAL sum of all calibration values is {part_2}")


if __name__ == '__main__':
    main()
