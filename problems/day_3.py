# https://adventofcode.com/2025/day/3

from utils import measure_time

DAY = 3
SAMPLE_DATA_PATH = f"../puzzle-input/{DAY}/sample.txt"
PUZZLE_DATA_PATH = f"../puzzle-input/{DAY}/puzzle.txt"


def get_highest_jolt_part_1(number_sequence: str) -> int:
    first_battery_digit = max(number_sequence[:-1])
    first_battery_digit_idx = number_sequence.find(first_battery_digit)
    second_battery_digit = max(number_sequence[first_battery_digit_idx + 1 :])

    return int(f"{first_battery_digit}{second_battery_digit}")


def get_highest_jolt_part_2(number_sequence: str) -> int:
    remaining_number_seq = number_sequence
    digits = 12
    jolt = ""
    for i in range(digits - 1, -1, -1):
        highest_battery_digit = max(remaining_number_seq[:-i] or remaining_number_seq)
        highest_battery_digit_idx = remaining_number_seq.find(highest_battery_digit)
        remaining_number_seq = remaining_number_seq[highest_battery_digit_idx + 1 :]
        jolt = f"{jolt}{highest_battery_digit}"

    return int(jolt)


@measure_time
def day_3(use_sample=False):
    """
    Part 1: In each battery sequence, e.g. '987654321111111' find the highest two-digit number possible -> 98.
    Part 2: In each battery sequence, find the highest twelve-digit number possible -> 987654321111
    """
    path = SAMPLE_DATA_PATH if use_sample else PUZZLE_DATA_PATH
    part_1 = 0
    part_2 = 0

    with open(path) as file:
        for line in file.readlines():
            battery_seq = line.replace("\n", "")
            jolt_p1 = get_highest_jolt_part_1(battery_seq)
            part_1 += jolt_p1

            jolt_p2 = get_highest_jolt_part_2(battery_seq)
            part_2 += jolt_p2
    return part_1, part_2


if __name__ == "__main__":
    p1, p2 = day_3(use_sample=False)
    print(f"Part 1: {p1}\nPart 2: {p2}")
