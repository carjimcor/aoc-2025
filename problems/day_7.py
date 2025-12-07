# https://adventofcode.com/2025/day/7
from utils import measure_time

DAY = 7
SAMPLE_DATA_PATH = f"../puzzle-input/{DAY}/sample.txt"
PUZZLE_DATA_PATH = f"../puzzle-input/{DAY}/puzzle.txt"

BEAM_START_SYMBOL = "S"
EMPTY_SYMBOL = "."
SPLIT_SYMBOL = "^"


def get_part_1(lines):
    result = 0
    beam_positions = [lines[0].find(BEAM_START_SYMBOL)]

    for line in lines[1:]:
        new_beam_positions = set()
        for beam_pos in beam_positions:
            if line[beam_pos] == EMPTY_SYMBOL:
                new_beam_positions.add(beam_pos)
            else:
                new_beam_positions.add(beam_pos - 1)
                new_beam_positions.add(beam_pos + 1)
                result += 1
        beam_positions = list(new_beam_positions)

    return result


def get_part_2(lines):
    def add_to_dict(beam_pos_dict, key, value):
        if key in beam_pos_dict:
            beam_pos_dict[key] += value
        else:
            beam_pos_dict[key] = value

    beam_positions = {lines[0].find(BEAM_START_SYMBOL): 1}

    for line in lines[1:]:
        new_beam_positions = dict()
        for beam_pos, amount in beam_positions.items():
            if line[beam_pos] == EMPTY_SYMBOL:
                add_to_dict(new_beam_positions, beam_pos, amount)
            else:
                add_to_dict(new_beam_positions, beam_pos - 1, amount)
                add_to_dict(new_beam_positions, beam_pos + 1, amount)
        beam_positions = new_beam_positions.copy()

    return sum(beam_positions.values())


@measure_time
def day_7(use_sample=False):
    """
    Part 1: Find how many times the beam splits.
    Part 2: Find how many alternate realities exist at the end of the Beam paths.
    """
    path = SAMPLE_DATA_PATH if use_sample else PUZZLE_DATA_PATH

    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]

    part_1 = get_part_1(lines)
    part_2 = get_part_2(lines)

    return part_1, part_2


if __name__ == "__main__":
    p1, p2 = day_7(use_sample=False)
    print(f"Part 1: {p1}\nPart 2: {p2}")
