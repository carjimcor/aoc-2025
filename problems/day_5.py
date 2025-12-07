# https://adventofcode.com/2025/day/5

from copy import deepcopy
from utils import measure_time

DAY = 5
SAMPLE_DATA_PATH = f"../puzzle-input/{DAY}/sample.txt"
PUZZLE_DATA_PATH = f"../puzzle-input/{DAY}/puzzle.txt"


def sort_ranges(ranges):
    """Sort ranges and merge those that overlap"""
    new_ranges = sorted(deepcopy(ranges), key=lambda x: x[0])
    result = []
    previous_max = 0
    for idx, (_min, _max) in enumerate(new_ranges):
        if idx and _min <= previous_max:
            # Merge with the previous range
            previous_max = max(_max, previous_max)
            result[-1] = (result[-1][0], previous_max)
            continue

        result.append((_min, _max))
        previous_max = _max

    return result


def get_data(path):
    with open(path) as file:
        ranges, ingredients = file.read().split("\n" * 2)
        ranges = [tuple(map(int, line.split("-"))) for line in ranges.split("\n")]
        ingredients = list(map(int, ingredients.strip().split("\n")))

    ranges = sort_ranges(ranges)

    return ranges, ingredients


@measure_time
def day_5(use_sample=False):
    """
    Part 1: Find ingredients in the ranges from the first part of the puzzle, those are fresh, the rest are spoiled.
    Part 2: Find the total number of valid numbers considering all the ranges.
    """
    path = SAMPLE_DATA_PATH if use_sample else PUZZLE_DATA_PATH
    part_1 = 0  # Fresh Ingredients
    part_2 = 0  # Fresh Ingredients counting only the valid ingredient ranges.

    ranges, ingredients = get_data(path)

    # Part 1
    current_range_idx = 0
    max_ranges_idx = len(ranges)
    current_min, current_max = ranges[current_range_idx]

    stop = False
    for idx, ingredient in enumerate(sorted(ingredients)):
        if ingredient > current_max:
            # Update current_min, current_max until current_max is <= ingredient
            while ingredient > current_max:
                current_range_idx += 1
                if current_range_idx >= max_ranges_idx:
                    # Reached the last range
                    stop = True
                    break
                current_min, current_max = ranges[current_range_idx]

            if stop:
                # Reached the last range
                break

        if current_min <= ingredient <= current_max:
            part_1 += 1
            continue

    # Part 2
    for start, end in ranges:
        part_2 += end - start + 1

    return part_1, part_2


if __name__ == "__main__":
    p1, p2 = day_5(use_sample=False)
    print(f"Part 1: {p1}\nPart 2: {p2}")
