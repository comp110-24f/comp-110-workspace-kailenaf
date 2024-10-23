"""A file called max_test that is used for CQ07!"""

__author__ = "730757297"

from find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    assert find_and_remove_max([10, 4, 5, 7, 10]) == 10


def test_find_and_remove_max1() -> None:
    a: list[int] = [2, 4, 6, 8, 8]
    assert find_and_remove_max(a) == 8, 8


def test_find_and_remove_max2() -> None:
    assert find_and_remove_max([]) == -1
