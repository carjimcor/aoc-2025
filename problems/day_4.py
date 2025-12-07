# https://adventofcode.com/2025/day/4

from copy import deepcopy
from utils import measure_time

DAY = 4
SAMPLE_DATA_PATH = f"../puzzle-input/{DAY}/sample.txt"
PUZZLE_DATA_PATH = f"../puzzle-input/{DAY}/puzzle.txt"

PAPER_ROLL_SYMBOL = "@"
REMOVE_SYMBOL = "_"
MAX_NEIGHBOUR_ROLLS_P1 = 4


def compute_rolls_proximity_map(rolls, rolls_prox_map):
    rows = len(rolls)
    cols = len(rolls[0])

    new_rolls = deepcopy(rolls)

    accessible_rolls = 0

    for row in range(rows):
        for col in range(cols):
            # Check if there is a paper roll in this position
            if rolls[row][col] != PAPER_ROLL_SYMBOL:
                rolls_prox_map[row][col] = 0
                continue

            slices = []
            col_min = max(col - 1, 0)
            col_max = min(col + 2, cols)
            if row:
                top_slice = "".join(rolls[row - 1][col_min:col_max])
                slices.append(top_slice)
            middle_slice = "".join(rolls[row][col_min:col_max])
            slices.append(middle_slice)
            if row < rows - 1:
                bottom_slice = "".join(rolls[row + 1][col_min:col_max])
                slices.append(bottom_slice)

            slices = "".join(slices)
            neighbours = slices.count(PAPER_ROLL_SYMBOL) - 1
            if neighbours < MAX_NEIGHBOUR_ROLLS_P1:
                accessible_rolls += 1
                # Part 2: Remove roll
                new_rolls[row][col] = REMOVE_SYMBOL

            rolls_prox_map[row][col] = neighbours

    return accessible_rolls, new_rolls


@measure_time
def day_4(use_sample=False):
    """
    Part 1: Find rolls of paper that have fewer than 4 rolls in adjacent positions.
    Part 2: Repeat the process, removing rolls each time until there are no more removable rolls.
    """
    path = SAMPLE_DATA_PATH if use_sample else PUZZLE_DATA_PATH

    rolls = []
    rolls_proximity_map = []

    with open(path) as file:
        rolls = [list(line.replace("\n", "")) for line in file.readlines()]
        rolls_proximity_map = [[""] * len(line) for line in rolls]

    part_1, rolls = compute_rolls_proximity_map(rolls, rolls_proximity_map)
    part_2 = removable_rolls = part_1
    while removable_rolls:
        removable_rolls, rolls = compute_rolls_proximity_map(rolls, rolls_proximity_map)
        part_2 += removable_rolls

    # print(*rolls, sep="\n")
    # print(*rolls_proximity_map, sep="\n")

    return part_1, part_2


if __name__ == "__main__":
    p1, p2 = day_4(use_sample=False)
    print(f"Part 1: {p1}\nPart 2: {p2}")
