from dataclasses import dataclass
import sys
from io import StringIO
from itertools import islice


def parse_called(line):
    return [int(number) for number in line.split(",")]


@dataclass
class Square:
    number: int
    called: bool = False

    def __repr__(self):
        return f"{self.number}:{self.called}"


def parse_board_line(line):
    return [Square(int(number)) for number in line.strip().split(" ") if number]


def mark(board, number):
    for square in board:
        if square.number == number:
            square.called = True


def is_winner(board):
    """
    1  2  3  4  5
    6  7  8  9  10
    11 12 13 14 15
    16 17 18 19 20
    21 22 23 24 25

    iterate over rows = start * 5 to start * 5 + 5
    iterate over columns = 0 to end, step 5
    """

    # Check rows
    for row_start in range(5):
        row = [square for square in islice(board, row_start * 5, row_start * 5 + 5)]
        if all([square.called for square in row]):
            return True
    
    # Check columns
    for column_start in range(5):
        column = [square for square in islice(board, column_start, None, 5)]
        if all([square.called for square in column]):
            return True

    return False

def call(boards, number):
    """Will mark the number on all boards. If a board wins it will be returned."""

    won = []
    lost = []
    for board in boards:
        mark(board, number)
        if is_winner(board):
            won.append(board)
        else:
            lost.append(board)

    return won, lost


def sum_unmarked(board):
    total = 0
    for square in board:
        if not square.called:
            total += square.number

    return total


def part2(data):
    boards = []

    with StringIO(data) as file:
        called_numbers = parse_called(file.readline())
        file.readline()

        board = []
        for line in file:
            if line == "\n":
                boards.append(board)
                board = []
            else:
                board += parse_board_line(line)

    won_boards = []
    for number in called_numbers:
        won, lost = call(boards, number)
        boards = lost
        won_boards = won
        if len(lost) == 0:
            break

    unmarked = sum_unmarked(won_boards[-1])

    return unmarked, number, unmarked * number


if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        data = file.read()

    print(part2(data))
