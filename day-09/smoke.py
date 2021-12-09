#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 9 script.
"""


import sys

import numpy as np


def part_1(heights: list[list[int]]) -> int:
    risk: list[int] = []

    for row_num, row in enumerate(heights):
        for col_num, val in enumerate(row):
            surrounding: list[int] = []

            if row_num == 0:
                surrounding.append(heights[row_num + 1][col_num])
            elif row_num == len(heights) - 1:
                surrounding.append(heights[row_num - 1][col_num])
            else:
                surrounding.append(heights[row_num + 1][col_num])
                surrounding.append(heights[row_num - 1][col_num])

            if col_num == 0:
                surrounding.append(heights[row_num][col_num + 1])
            elif col_num == len(row) - 1:
                surrounding.append(heights[row_num][col_num - 1])
            else:
                surrounding.append(heights[row_num][col_num + 1])
                surrounding.append(heights[row_num][col_num - 1])

            if all(val < x for x in surrounding):
                risk.append(val + 1)

    return sum(risk)


def main() -> None:
    name: str = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    heights: list[list[int]] = []
    try:
        with open(name, "r") as f:
            heights = [[int(i) for i in line.strip()] for line in f.readlines()]
    except FileNotFoundError:
        print(f"File '{name}' not found.")
        exit(1)

    print(f"Part 1: {part_1(heights)}")


if __name__ == "__main__":
    main()
