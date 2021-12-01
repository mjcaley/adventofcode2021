from adventofcode2021.one.part2 import part2


def test_part2():
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

    assert 5 == part2(test_input)
