#!/usr/bin/env python3


"""
Day 1 script.

Usage:

    ./sweep.py [N] [S]

    - [optional] N (str): File name of the input - default 'input.txt'
    - [optional] S (int): Window size for part 2 - default 3
"""


import sys


def to_nums(name: str) -> list[int]:
    """
    Convert the input numbers from the file with the given name into a list of
    measurements.

    Params:
        name (str): Name of the input file.

    Returns:
        list[int]: List of measuremnts.
    """

    try:
        with open(name) as f:
            return [int(s.strip()) for s in f.readlines()]
    except FileNotFoundError:
        print(f"Invalid file name '{name}', file not found")
        exit(1)
    except ValueError:
        print("Invalid contents, input contains non-integer values")
        exit(1)


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

    name: str = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    nums: list[int] = to_nums(name)

    win_size: int = 3
    if len(sys.argv) >= 3:
        try:
            win_size: int = int(sys.argv[2])
        except ValueError:
            print(f"Invalid argument '{sys.argv[2]}' for window sizes, non-integer")
            exit(1)

    print(f"Part 1: {count_increments(nums)}")
    print(f"Part 2: {count_increments(get_window_sums(nums, win_size))}")


if __name__ == "__main__":
    main()
