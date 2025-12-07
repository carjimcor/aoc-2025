# https://adventofcode.com/2025/day/2

from utils import measure_time

DAY = 2
SAMPLE_DATA_PATH = f"../puzzle-input/{DAY}/sample.txt"
PUZZLE_DATA_PATH = f"../puzzle-input/{DAY}/puzzle.txt"


@measure_time
def day_2(use_sample=False):
    """
    Part 1: Find repeated number sequences in the ranges from the input. Examples 55, 99, 1010, 123123.
    Part 2: Similar to 1, but this time the repeated number can be repeated more than once. Examples: 111, 121212.
    """
    path = SAMPLE_DATA_PATH if use_sample else PUZZLE_DATA_PATH
    ranges = []
    target_sequences_part_1 = []
    target_sequences_part_2 = []

    with open(path) as file:
        ranges = [
            tuple(map(int, _range.split("-"))) for _range in file.readline().split(",")
        ]

    for a, b in ranges:
        for number in range(a, b + 1):
            number_str = str(number)
            len_number = len(number_str)
            half_len = len_number // 2

            # Part 1
            first_half, second_half = number_str[:half_len], number_str[half_len:]
            if first_half == second_half:
                target_sequences_part_1.append(number)

            # Part 2
            for slice_amount in range(1, half_len + 1):
                number_slices = [
                    number_str[i : i + slice_amount]
                    for i in range(0, len_number, slice_amount)
                ]
                number_slice_set = set(number_slices)
                if len(number_slice_set) == 1:
                    target_sequences_part_2.append(number)
                    break

    return sum(target_sequences_part_1), sum(target_sequences_part_2)


if __name__ == "__main__":
    p1, p2 = day_2(use_sample=False)
    print(f"Part 1: {p1}\nPart 2: {p2}")
