#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 8 script.
"""


import sys


def part_1(patterns: list[tuple[list[str], list[str]]]) -> int:
    count: int = 0
    for (_, right) in patterns:
        count += sum([len(i) in [2, 4, 3, 7] for i in right])
    return count


def main() -> None:
    name: str = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    patterns: list[tuple[list[str], list[str]]] = []
    try:
        with open(name, "r") as f:
            patterns = [
                (left.split(), right.split())
                for left, _, right in [i.partition(" | ") for i in f.readlines()]
            ]
    except FileNotFoundError:
        print(f"File '{name}' not found.")
        exit(1)

    print(f"Part 1: {part_1(patterns)}")


if __name__ == "__main__":
    main()
