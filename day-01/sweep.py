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


def count_increments(nums: list[int]) -> int:
    """
    Count the number of times a number is larger from the previous number.

    Params:
        nums (list[int]): List of numbers.

    Returns:
        int: Number of increments.
    """

    return sum([num > pre for num, pre in zip(nums[1:], nums[:-1])])


def get_window_sums(nums: list[int], win_size: int = 3) -> list[int]:
    """
    Convert the given measurements to the list of window sums.

    Params:
        nums (list[int]): List of measurements.
        win_size (int): Size of each window.

    Returns:
        list[int]: Sum of each window.
    """

    return [sum(nums[i : i + win_size]) for i in range(len(nums) - (win_size - 1))]


def main() -> None:
    """
    Main entrypoint of the program.
    """

    nums: list[int] = to_nums("input.txt")
    print(f"Part 1: {count_increments(nums)}")
    print(f"Part 2: {count_increments(get_window_sums(nums))}")


if __name__ == "__main__":
    main()
