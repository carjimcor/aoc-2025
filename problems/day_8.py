# https://adventofcode.com/2025/day/8

from utils import measure_time

DAY = 8
SAMPLE_DATA_PATH = f"../puzzle-input/{DAY}/sample.txt"
PUZZLE_DATA_PATH = f"../puzzle-input/{DAY}/puzzle.txt"


@measure_time
def day_8(use_sample=False):
    """


    Part 1:
    Part 2:
    """
    path = SAMPLE_DATA_PATH if use_sample else PUZZLE_DATA_PATH
    part_1 = 0
    part_2 = 0

    with open(path) as file:
        pass

    return part_1, part_2


if __name__ == "__main__":
    p1, p2 = day_8(use_sample=True)
    print(f"Part 1: {p1}\nPart 2: {p2}")
