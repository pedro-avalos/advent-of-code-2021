#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 7 script.
"""


def main():
    positions: list[int] = []
    with open("input.txt") as f:
        positions = [int(i) for i in f.read().strip().split(",")]

    possibilities_1: list[int] = [0] * (max(positions) - min(positions) - 1)
    possibilities_2: list[int] = [0] * (max(positions) - min(positions) - 1)
    for i in range(len(possibilities_1)):
        for j in positions:
            possibilities_1[i] += abs(i - j)
            possibilities_2[i] += sum([n + 1 for n in range(abs(i - j))])

    print(f"Part 1: {min(possibilities_1)}")
    print(f"Part 2: {min(possibilities_2)}")


if __name__ == "__main__":
    main()
