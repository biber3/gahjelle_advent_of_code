"""Tests for AoC 3, 2017: Spiral Memory"""

# Standard library imports
import pathlib

# Third party imports
import aoc201703
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201703.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201703.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == 23


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201703.part1(example1) == 2


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc201703.part1(example2) == 31


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201703.part2(example1) == 25


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc201703.part2(example2) == 1968
