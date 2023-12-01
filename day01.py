#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '01 December 2023'
__version__ = '0.1.0'


def get_input_data(filename: str) -> list:
    with open(filename, 'r') as my_file:
        puzzle_input = my_file.read()
    puzzle_input = [x.strip() for x in puzzle_input.strip().split('\n')]
    return puzzle_input


def isDigit(s: str) -> bool:
    if s >= '0' and s <= '9':
        return True
    return False


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


def main() -> None:
    puzzle_input = get_input_data("input_01.txt")
    part_1 = day_01_part_1(puzzle_input=puzzle_input)
    print(f"The sum of all calibration values is {part_1}")


if __name__ == '__main__':
    main()
