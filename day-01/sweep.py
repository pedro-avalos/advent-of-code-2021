#!/usr/bin/env python3


def main() -> None:
    with open("input.txt") as f:
        increase_count: int = 0
        pre_num: int = int(f.readline().strip())
        print(f"{pre_num} (N/A - no previous measurement)")

        for line in f.readlines():
            num: int = int(line.strip())
            print(f"{num} ", end="")
            if num > pre_num:
                increase_count += 1
                print("(increased)")
            else:
                print("(decreased)")
            pre_num = num

        print(increase_count)


if __name__ == "__main__":
    main()
