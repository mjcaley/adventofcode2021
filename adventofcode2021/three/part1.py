import sys


def bits_to_int(bits):
    num = 0
    for i, n in enumerate(reversed(bits)):
        num |= n << i

    return num


def part1(data):
    ones = [0] * len(data[0])

    for line in data:
        for index, value in enumerate(line):
            if value == 1:
                ones[index] += 1

    gamma_bits = [1 if n > len(data)//2 else 0 for n in ones]
    epsilon_bits = [1 if n == 0 else 0 for n in gamma_bits]
    gamma = bits_to_int(gamma_bits)
    epsilon = bits_to_int(epsilon_bits)

    return gamma, epsilon, gamma * epsilon


if __name__ == "__main__":
    data = []

    with open(sys.argv[1], "r") as file:
        for line in file:
            data.append([int(char) for char in line.strip()])

    print(part1(data))
