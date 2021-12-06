import pytest

from adventofcode2021.three.part1 import part1
from adventofcode2021.three.part2 import part2


@pytest.fixture
def test_input():
    return [
        [0,0,1,0,0],
        [1,1,1,1,0],
        [1,0,1,1,0],
        [1,0,1,1,1],
        [1,0,1,0,1],
        [0,1,1,1,1],
        [0,0,1,1,1],
        [1,1,1,0,0],
        [1,0,0,0,0],
        [1,1,0,0,1],
        [0,0,0,1,0],
        [0,1,0,1,0],
    ]


def test_part1(test_input):
    gamma, epsilon, result = part1(test_input)

    assert 9 == epsilon
    assert 22 == gamma
    assert 198 == result


def test_part2(test_input):
    o2_rating, co2_rating, result = part2(test_input)

    assert 23 == o2_rating
    assert 10 == co2_rating
    assert 230 == result
