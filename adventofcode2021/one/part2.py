from itertools import tee
import sys


def tripleiter(iter):
    first, second, third = tee(iter, 3)
    next(second)
    next(third)
    next(third)

    return zip(first, second, third)


def part2(data):
    num_increased = 0

    first_window = tripleiter(data)
    second_window = tripleiter(data)
    next(second_window)

    for left, right in zip(first_window, second_window):
        left_sum = left[0] + left[1] + left[2]
        right_sum = right[0] + right[1] + right[2]

        if right_sum > left_sum:
            num_increased += 1

    return num_increased


if __name__ == "__main__":
    data = []

    with open(sys.argv[1], "r") as file:
        for line in file.readlines():
            data.append(int(line))

    print(part2(data))
