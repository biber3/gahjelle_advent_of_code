"""Tests for AoC 17, 2020: Conway Cubes"""

# Standard library imports
import pathlib

# Third party imports
import aoc202017
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202017.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == {
        (0, 1, 0, 0),
        (1, 2, 0, 0),
        (2, 0, 0, 0),
        (2, 1, 0, 0),
        (2, 2, 0, 0),
    }


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202017.part1(example1) == 112


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202017.part2(example1) == 848
