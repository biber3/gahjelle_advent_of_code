"""Tests for AoC 23, 2023: A Long Walk."""

# Standard library imports
import pathlib

# Third party imports
import aoc202323
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202323.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        (0, 1): ".",
        (1, 1): ".",
        (1, 2): ".",
        (1, 3): ".",
        (1, 4): ".",
        (1, 5): ".",
        (1, 6): ".",
        (1, 7): ".",
        (1, 17): ".",
        (1, 18): ".",
        (1, 19): ".",
        (2, 7): ".",
        (2, 17): ".",
        (2, 19): ".",
        (3, 3): ".",
        (3, 4): ".",
        (3, 5): ".",
        (3, 6): ".",
        (3, 7): ".",
        (3, 9): ".",
        (3, 10): ">",
        (3, 11): ".",
        (3, 12): ">",
        (3, 13): ".",
        (3, 17): ".",
        (3, 19): ".",
        (4, 3): "v",
        (4, 9): ".",
        (4, 11): "v",
        (4, 13): ".",
        (4, 17): ".",
        (4, 19): ".",
        (5, 3): ".",
        (5, 4): ">",
        (5, 5): ".",
        (5, 6): ".",
        (5, 7): ".",
        (5, 9): ".",
        (5, 11): ".",
        (5, 13): ".",
        (5, 14): ".",
        (5, 15): ".",
        (5, 16): ".",
        (5, 17): ".",
        (5, 19): ".",
        (5, 20): ".",
        (5, 21): ".",
        (6, 3): "v",
        (6, 7): ".",
        (6, 9): ".",
        (6, 11): ".",
        (6, 21): ".",
        (7, 3): ".",
        (7, 4): ".",
        (7, 5): ".",
        (7, 7): ".",
        (7, 9): ".",
        (7, 11): ".",
        (7, 12): ".",
        (7, 13): ".",
        (7, 14): ".",
        (7, 15): ".",
        (7, 16): ".",
        (7, 17): ".",
        (7, 19): ".",
        (7, 20): ".",
        (7, 21): ".",
        (8, 5): ".",
        (8, 7): ".",
        (8, 9): ".",
        (8, 17): ".",
        (8, 19): ".",
        (9, 1): ".",
        (9, 2): ".",
        (9, 3): ".",
        (9, 4): ".",
        (9, 5): ".",
        (9, 7): ".",
        (9, 9): ".",
        (9, 11): ".",
        (9, 12): ".",
        (9, 13): ".",
        (9, 14): ".",
        (9, 15): ".",
        (9, 16): ".",
        (9, 17): ".",
        (9, 19): ".",
        (9, 20): ".",
        (9, 21): ".",
        (10, 1): ".",
        (10, 7): ".",
        (10, 9): ".",
        (10, 11): ".",
        (10, 21): "v",
        (11, 1): ".",
        (11, 3): ".",
        (11, 4): ".",
        (11, 5): ".",
        (11, 7): ".",
        (11, 8): ".",
        (11, 9): ".",
        (11, 11): ".",
        (11, 12): ".",
        (11, 13): ".",
        (11, 17): ".",
        (11, 18): ".",
        (11, 19): ".",
        (11, 20): ">",
        (11, 21): ".",
        (12, 1): ".",
        (12, 3): ".",
        (12, 5): "v",
        (12, 13): "v",
        (12, 17): ".",
        (12, 21): "v",
        (13, 1): ".",
        (13, 2): ".",
        (13, 3): ".",
        (13, 5): ".",
        (13, 6): ">",
        (13, 7): ".",
        (13, 9): ".",
        (13, 10): ".",
        (13, 11): ".",
        (13, 12): ">",
        (13, 13): ".",
        (13, 14): ">",
        (13, 15): ".",
        (13, 17): ".",
        (13, 21): ".",
        (14, 5): "v",
        (14, 7): ".",
        (14, 9): ".",
        (14, 13): "v",
        (14, 15): ".",
        (14, 17): ".",
        (14, 21): ".",
        (15, 1): ".",
        (15, 2): ".",
        (15, 3): ".",
        (15, 4): ".",
        (15, 5): ".",
        (15, 7): ".",
        (15, 8): ".",
        (15, 9): ".",
        (15, 11): ".",
        (15, 12): ".",
        (15, 13): ".",
        (15, 15): ".",
        (15, 17): ".",
        (15, 19): ".",
        (15, 20): ".",
        (15, 21): ".",
        (16, 1): ".",
        (16, 11): ".",
        (16, 15): ".",
        (16, 17): ".",
        (16, 19): ".",
        (17, 1): ".",
        (17, 2): ".",
        (17, 3): ".",
        (17, 7): ".",
        (17, 8): ".",
        (17, 9): ".",
        (17, 11): ".",
        (17, 12): ".",
        (17, 13): ".",
        (17, 15): ".",
        (17, 16): ".",
        (17, 17): ".",
        (17, 19): ".",
        (18, 3): ".",
        (18, 7): ".",
        (18, 9): ".",
        (18, 13): "v",
        (18, 19): "v",
        (19, 1): ".",
        (19, 2): ".",
        (19, 3): ".",
        (19, 5): ".",
        (19, 6): ".",
        (19, 7): ".",
        (19, 9): ".",
        (19, 11): ".",
        (19, 12): ">",
        (19, 13): ".",
        (19, 14): ">",
        (19, 15): ".",
        (19, 17): ".",
        (19, 18): ">",
        (19, 19): ".",
        (20, 1): ".",
        (20, 5): ".",
        (20, 9): ".",
        (20, 11): ".",
        (20, 15): ".",
        (20, 17): ".",
        (20, 19): "v",
        (21, 1): ".",
        (21, 2): ".",
        (21, 3): ".",
        (21, 4): ".",
        (21, 5): ".",
        (21, 9): ".",
        (21, 10): ".",
        (21, 11): ".",
        (21, 15): ".",
        (21, 16): ".",
        (21, 17): ".",
        (21, 19): ".",
        (21, 20): ".",
        (21, 21): ".",
        (22, 21): ".",
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202323.part1(example1) == 94


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202323.part2(example1) == 154
