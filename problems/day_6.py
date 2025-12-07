# https://adventofcode.com/2025/day/6

from utils import measure_time
from math import prod

DAY = 6
SAMPLE_DATA_PATH = f"../puzzle-input/{DAY}/sample.txt"
PUZZLE_DATA_PATH = f"../puzzle-input/{DAY}/puzzle.txt"


def get_part_1(path):
    result = 0

    with open(path) as file:
        lines = [line.split() for line in file.readlines()]

    *lines, operators = lines

    lines = [list(map(int, line)) for line in lines]

    for idx, operator in enumerate(operators):
        numbers = [line[idx] for line in lines]

        if operator == "*":
            result += prod(numbers)
        else:
            result += sum(numbers)

    return result


def get_part_2(path):
    result = 0

    with open(path) as file:
        lines = [line.replace("\n", "") for line in file.readlines()]

    *lines, operators = lines

    numbers = []
    for idx in range(len(lines[0]) - 1, -1, -1):
        number = int("".join([line[idx] for line in lines]).strip() or 0)

        if not number:
            numbers = []
            continue

        numbers.append(number)

        operator = operators[idx].strip()

        if not operator:
            continue
        elif operator == "*":
            result += prod(numbers)
        else:
            result += sum(numbers)

    return result


@measure_time
def day_6(use_sample=False):
    """
    Part 1: For each column, sum or multiply all the numbers together, return the sum of all those results.
    Part 2: For each column block, consider the numbers vertically from top to bottom, and right to left.
    """
    path = SAMPLE_DATA_PATH if use_sample else PUZZLE_DATA_PATH

    part_1 = get_part_1(path)
    part_2 = get_part_2(path)

    return part_1, part_2


if __name__ == "__main__":
    p1, p2 = day_6(use_sample=False)
    print(f"Part 1: {p1}\nPart 2: {p2}")
