import pytest

from adventofcode2021.two.part1 import part1
from adventofcode2021.two.part2 import part2


@pytest.fixture
def test_input():
    return [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]


def test_part1(test_input):
    position, depth, result = part1(test_input)

    assert 15 == position
    assert 10 == depth
    assert 150 == result


def test_part2(test_input):
    position, depth, result = part2(test_input)

    assert 15 == position
    assert 60 == depth
    assert 900 == result
