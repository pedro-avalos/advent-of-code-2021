#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 4 script.

Examples:

    $ ./bingo.py [N]

    - [optional] N (str): File name of the input - default 'input.txt'
"""


import sys

import numpy as np


def get_input(file_name: str) -> tuple[list[int], list[np.ndarray]]:
    """
    Retrieve the numbers called and the boards.

    Args:
        file_name (str): Name of the file with the input data.

    Returns:
        tuple[list[int], list[np.ndarray]]: Order and boards respectively.
    """

    with open(file_name) as f:
        order = list(map(int, f.readline().strip().split(",")))
        board_nums: list[int] = list(
            map(int, f.read().replace("\n", " ").strip().split())
        )
        tmp: list[list[int]] = [
            board_nums[i : i + 5] for i in range(0, len(board_nums), 5)
        ]
        boards = [np.array(tmp[i : i + 5]) for i in range(0, len(tmp), 5)]
    return order, boards


def mark(board: np.ndarray, num: int) -> None:
    """
    Check if the board contains the current number.

    If the board contains the number, then "mark" it by setting the cell to -1.

    Args:
        board (np.ndarray): Board to be checked.
        num (int): Number called out.
    """

    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == num:
                board[i][j] = -1


def has_won(board: np.ndarray) -> bool:
    """
    Check if the given board has won.

    Args:
        board (np.ndarray): Board to be checked.

    Returns:
        bool: True if the board has a row or column of all marked numbers.
    """

    trans: np.ndarray = board.transpose()
    for i in range(len(board)):
        if sum(board[i]) == -5 or sum(trans[i]) == -5:
            return True
    return False


def score(board: np.ndarray, num: int) -> int:
    """
    Score the given board.

    Args:
        board (np.ndarray): Board to be scored.
        num (int): Number called when this board won.

    Returns:
        int: Score of the board.
    """

    board_sum: int = 0
    for row in board:
        for val in row:
            board_sum += val if val != -1 else 0
    return board_sum * num


def main() -> None:
    """
    Find the first and last boards to win, then score them.
    """

    file_name: str = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    order: list[int] = []
    boards: list[np.ndarray] = []

    try:
        order, boards = get_input(file_name)
    except FileNotFoundError:
        print(f"File '{file_name}' not found")
        exit(1)

    win_status: list[bool] = [False] * len(boards)
    first_num: int = -1
    first_win: np.ndarray = np.ndarray([])
    last_num: int = -1
    last_win: np.ndarray = np.ndarray([])
    for num in order:
        # When all boards have been won, stop reading the numbers
        if all(win_status):
            break

        for board_num, board in enumerate(boards):
            # Don't bother to repeat boards that have been won already
            if win_status[board_num]:
                continue

            # Check if the board contains the current number and mark it if so
            mark(board, num)

            # Check if the board has won as a result
            if has_won(board):
                win_status[board_num] = True  # This board has won

                # This is the first board to win
                if sum(win_status) == 1:
                    first_win = board
                    first_num = num
                # This is the last board to win
                elif all(win_status):
                    last_win = board
                    last_num = num

    print(f"Part 1: {score(first_win, first_num)}")
    print(f"Part 2: {score(last_win, last_num)}")


if __name__ == "__main__":
    main()
