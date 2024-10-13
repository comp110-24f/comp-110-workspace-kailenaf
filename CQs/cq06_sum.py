"""Summing the elements of a list using different loops"""

__author__ = "730757297"


def w_sum(vals: list[float]) -> float:
    elem: int = 0
    total: float = 0.0
    while elem < len(
        vals
    ):  # while the elements are less than the length of vals in the list
        total = vals[elem] + total
        elem += 1
    return total


def f_sum(vals: list[float]) -> float:
    total: float = 0.0
    for (
        elem
    ) in vals:  # for every number (elem) in vals (list) return the total + each element
        total += elem
    return total


def f_range_sum(vals: list[float]) -> float:
    total: float = 0.0
    for elem in range(
        0, len(vals)
    ):  # for every number (elem) in the range of the length of vals, starting at 0
        total += elem
    return total
