#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 7 script.
"""


def main():
    positions: list[int] = []
    with open("input.txt") as f:
        positions = [int(i) for i in f.read().strip().split(",")]

    possibilities: list[int] = [0] * (max(positions) - min(positions) - 1)
    for i in range(len(possibilities)):
        for j in positions:
            possibilities[i] += abs(i - j)

    print(f"Part 1: {min(possibilities)}")


if __name__ == "__main__":
    main()
