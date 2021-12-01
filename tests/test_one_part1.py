from adventofcode2021.one.part1 import part1


def test_sample():
    test_input = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]

    assert 7 == part1(test_input)
