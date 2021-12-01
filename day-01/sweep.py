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

    return sum([num > pre for num, pre in zip(nums[1:], nums[:-1])])


def part_2(nums: list[int], win_size: int = 3) -> int:
    """
    Count the number of times the sum of a window increased from the previous
    sum of a window.

    Params:
        nums (list[int]): List of measurements.
        win_size (int): Size of each window.

    Returns:
        int: Number of increments.
    """

    return 0


def main() -> None:
    """
    Main entrypoint of the program.
    """

    nums: list[int] = to_nums("input.txt")
    print(f"Part 1: {part_1(nums)}")
    print(f"Part 2: {part_2(nums)}")


if __name__ == "__main__":
    main()
