"""A file called utils_test that is used for EX05!"""

__author__ = "730757297"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_empty() -> None:
    """Testing an empty list with an edge case."""
    assert only_evens([]) == []  # edge case: if the list is empty


def test_only_evens_negatives() -> None:
    """Testing a list with negative numbers."""
    assert only_evens([-2, 0, 1, 2]) == [-2, 0, 2]  # use case: negative numbers


def test_only_evens_mixing() -> None:
    """Testing a list with mixed numbers."""
    assert only_evens([0, 6, 2, 5, 0]) == [0, 6, 2, 0]  # use case: mixed numbers


def test_sub_empty() -> None:
    """Testing an empty list with an edge case"""
    assert sub([], 0, 0) == []  # edge case: using an empty list


def test_sub_valid() -> None:
    """Testing function with valid indicies."""
    assert sub([1, 4, 5, 6, 7, 8, 9], 1, 4) == [
        4,
        5,
        6,
    ]  # use case: using valid numbers


def test_sub_bounds() -> None:
    """Testing function with different bounds."""
    assert sub([1, 2, 3], -1, 10) == [1, 2, 3]  # use case: using different bounds


def test_add_at_index_out_of_bounds():
    """Testing by out of bound numbers."""
    with pytest.raises(IndexError):
        add_at_index([1, 2, 3], 4, 5)  # edge case: out of bounds #


def test_add_at_index_valid():
    """Testing the function with valid numbers."""
    list1 = [1, 2, 3, 8]
    add_at_index(list1, 4, 3)
    assert list1 == [1, 2, 3, 4, 8]  # use case: valid numbers


def test_add_at_index_mutating():
    """Testing by mutating the function."""
    list1 = [1, 2, 3]
    add_at_index(list1, 0, 0)
    assert list1 == [0, 1, 2, 3]  # use case: using a mutation
