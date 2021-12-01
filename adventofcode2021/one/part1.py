from itertools import pairwise
import sys


def part1(data):
    num_increased = 0

    for first, second in pairwise(data):
        if second > first:
            num_increased += 1

    return num_increased


if __name__ == "__main__":
    data = []

    with open(sys.argv[1], "r") as file:
        for line in file.readlines():
            data.append(int(line))

    print(part1(data))
