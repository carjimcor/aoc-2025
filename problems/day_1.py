# https://adventofcode.com/2025/day/1

# Notes: The dial goes from 0 to 99, and can go from 99 to 0 in a Right rotation, or from 0 to 99 in a Left rotation
# Info about modulo:
# -68 % 100 = 32
# Remainder = Dividend - (Divisor * Quotient)
# Quotient: -68 // 100 = -1
# 32 = -68 -(100 * -1)

DAY = 1
SAMPLE_DATA_PATH = f"../puzzle-input/{DAY}/sample.txt"
PUZZLE_DATA_PATH = f"../puzzle-input/{DAY}/puzzle.txt"


def process_rotation(current_pos, turn_direction, amount):
    """Transform the rotation starting from current_pos."""
    sign = 1 if turn_direction == "R" else -1
    new_pos = current_pos
    times_over_0 = 0

    for _ in range(amount):
        new_pos = (new_pos + sign) % 100
        if not new_pos:
            times_over_0 += 1

    return new_pos, times_over_0


def day_1(use_sample=False):
    """
    Part 1: Count how many times the dial is left pointing at 0 after any rotation in the sequence.
    Part 2: Count how many times the dial goes through or ends up at 0 during all the rotations.
    """
    password_part_1 = 0
    password_part_2 = 0
    pos = 50  # dial starts at 50

    path = SAMPLE_DATA_PATH if use_sample else PUZZLE_DATA_PATH

    with open(path) as file:
        for line in file.readlines():
            turn_direction, amount = line[0], int(line[1:])

            pos, extra_times = process_rotation(pos, turn_direction, amount)
            password_part_2 += extra_times
            if not pos:
                # pos at 0
                password_part_1 += 1

    return password_part_1, password_part_2


if __name__ == "__main__":
    p1, p2 = day_1(use_sample=False)
    print(f"Part 1: {p1}\nPart 2: {p2}")
