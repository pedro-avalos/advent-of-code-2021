#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 6 script.
"""


import sys


def part_1(fish: list[int]) -> int:
    copy: list[int] = list(fish)
    for _ in range(80):
        for j in range(len(copy)):
            copy[j] -= 1
            if copy[j] < 0:
                copy[j] = 6
                copy.append(8)
    return len(copy)


def part_2(fish: list[int]) -> int:
    days: list[int] = [0] * 9
    for f in fish:
        days[f] += 1
    for i in range(256):
        today = i % len(days)
        days[(today + 7) % len(days)] += days[today]
    return sum(days)


def main() -> None:
    name: str = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    fish: list[int] = []
    try:
        with open(name, "r") as f:
            fish = [int(i) for i in f.read().strip().split(",")]
    except FileNotFoundError:
        print(f"File '{name}' not found.")
        exit(1)

    print(f"Part 1: {part_1(fish)}")
    print(f"Part 2: {part_2(fish)}")


if __name__ == "__main__":
    main()
