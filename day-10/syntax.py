#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 10 script.
"""


import sys


CHUNK_CHARS: dict[str, str] = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

SCORES: dict[str, int] = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def part_1(lines: list[str]) -> list[str]:
    out: list[str] = []
    for line in lines:
        stack: list[str] = []
        for c in line:
            if c in CHUNK_CHARS.keys():
                stack.append(c)
            elif c in CHUNK_CHARS.values():
                expected: str = CHUNK_CHARS[stack.pop()]
                if c != expected:
                    out.append(c)
    return out


def main() -> None:
    name: str = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    lines: list[str] = []
    try:
        with open(name, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File '{name}' not found.")
        exit(1)

    print(f"Part 1: {sum([SCORES[c] for c in part_1(lines)])}")


if __name__ == "__main__":
    main()
