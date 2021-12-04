#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bingo.

Examples:

    $ ./bingo.py [N]

    - [optional] N (str): File name of the input - default 'input.txt'
"""


import sys

import numpy as np


def has_won(board: np.ndarray) -> bool:
    trans: np.ndarray = board.transpose()
    for i in range(len(board)):
        if sum(board[i]) == -5 or sum(trans[i]) == -5:
            return True
    return False


def sum_board(board: np.ndarray) -> int:
    out: int = 0
    for row in board:
        for val in row:
            if val != -1:
                out += val
    return out


def main() -> None:
    file_name: str = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    order: list[int] = []
    boards: list[np.ndarray] = []

    try:
        with open(file_name) as f:
            order = list(map(int, f.readline().strip().split(",")))
            nums: list[int] = list(
                map(int, f.read().replace("\n", " ").strip().split())
            )
            tmp: list[list[int]] = [nums[i : i + 5] for i in range(0, len(nums), 5)]
            boards = [np.array(tmp[i : i + 5]) for i in range(0, len(tmp), 5)]
    except FileNotFoundError:
        print("")
        exit(1)

    done: bool = False
    win_status = [False] * len(boards)
    win_num: int = -1
    last_num: int = -1
    first_win: np.ndarray = np.ndarray([])
    last_win: np.ndarray = np.ndarray([])
    for num in order:
        if all(win_status):
            break

        for board_num, board in enumerate(boards):
            if win_status[board_num]:
                continue

            for i, row in enumerate(board):
                for j, val in enumerate(row):
                    if val == num:
                        board[i][j] = -1

            if has_won(board):
                if all(not i for i in win_status):
                    win_num = num
                    first_win = board

                win_status[board_num] = True
                if all(win_status):
                    last_win = board
                    last_num = num

    print(f"Part 1: {sum_board(first_win) * win_num}")
    print(f"Part 2: {sum_board(last_win) * last_num}")


if __name__ == "__main__":
    main()
