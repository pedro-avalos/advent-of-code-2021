#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 6 script.
"""


import sys


def main() -> None:
    name: str = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    fish: list[int] = []
    try:
        with open(name, "r") as f:
            fish = [int(i) for i in f.read().strip().split(",")]
    except FileNotFoundError:
        print(f"File '{name}' not found.")
        exit(1)

    for _ in range(80):
        for j in range(len(fish)):
            fish[j] -= 1
            if fish[j] < 0:
                fish[j] = 6
                fish.append(8)


    print(len(fish))


if __name__ == "__main__":
    main()
