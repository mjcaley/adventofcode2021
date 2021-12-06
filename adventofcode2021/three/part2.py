import sys


def bits_to_int(bits):
    num = 0
    for i, n in enumerate(reversed(bits)):
        num |= n << i

    return num


def group_by_index(data, index):
    zeros, ones = [], []
    for item in data:
        if item[index] == 0:
            zeros.append(item)
        else:
            ones.append(item)

    return zeros, ones


def filter_o2(data):
    filtered = data
    length = len(data[0])
    for i in range(length):
        if len(filtered) == 1:
            break
        zeros, ones = group_by_index(filtered, i)
        if len(zeros) > len(ones):
            filtered = zeros
        elif len(zeros) < len(ones):
            filtered = ones
        else:
            filtered = ones

    return bits_to_int(filtered[0])


def filter_co2(data):
    filtered = data
    length = len(data[0])
    for i in range(length):
        if len(filtered) == 1:
            break
        zeros, ones = group_by_index(filtered, i)
        if len(zeros) > len(ones):
            filtered = ones
        elif len(zeros) < len(ones):
            filtered = zeros
        else:
            filtered = zeros

    return bits_to_int(filtered[0])


def part2(data):
    ones = [0] * len(data[0])

    o2_rating = filter_o2(data)
    co2_rating = filter_co2(data)

    return o2_rating, co2_rating, o2_rating * co2_rating


if __name__ == "__main__":
    data = []

    with open(sys.argv[1], "r") as file:
        for line in file:
            data.append([int(char) for char in line.strip()])

    print(part2(data))
