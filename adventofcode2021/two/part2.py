import sys


def part2(data):
    horizonal_position = 0
    depth = 0
    aim = 0

    for command in data:
        direction, distance = command
        if direction == "forward":
            horizonal_position += distance
            depth += aim * distance
        elif direction == "up":
            aim -= distance
        elif direction == "down":
            aim += distance

    return horizonal_position, depth, horizonal_position * depth


if __name__ == "__main__":
    data = []

    with open(sys.argv[1], "r") as file:
        for line in file:
            direction, distance_string = line.split()
            data.append((direction, int(distance_string)))

    position, depth, result = part2(data)
    print(position, depth, result)
