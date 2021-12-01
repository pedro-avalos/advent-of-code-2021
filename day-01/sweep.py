#!/usr/bin/env python3


def to_nums(name: str) -> list[int]:
    """
    Convert the input numbers from the file with the given name into a list of
    measurements.

    Params:
        name (str): Name of the input file.

    Returns:
        list[int]: List of measuremnts.
    """

    with open(name) as f:
        return [int(s.strip()) for s in f.readlines()]


def part_1(nums: list[int]) -> int:
    """
    Count the number of times the measurement increased from the previous
    measurement.

    Params:
        nums (list[int]): List of measurements

    Returns:
        int: Number of increments.
    """

    return sum([
        num > pre for i, (num, pre) in enumerate(zip(nums[1:], nums[:-1]))
    ])


def main() -> None:
    """
    Main entrypoint of the program.
    """

    nums: list[int] = to_nums("input.txt")
    print(f"Part 1: {part_1(nums)}")


if __name__ == "__main__":
    main()
