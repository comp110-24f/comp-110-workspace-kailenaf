"""Mutating functions."""

__author__ = "730757297"

list1: list[int] = [1, 2, 3]
num1: int = 2


def manual_append(list1: list[int], num1: int) -> None:
    """mutate by adding to the end of the list"""
    list1.append(num1)  # using append to add an int to the end of a list
    print(list1)


list2: list[int] = [1, 2, 3]


def double(list2: list[int]) -> None:
    "mutate by doubling the list"
    index = 0
    while index < len(list2):
        list2[index] = list2[index] * 2  # used to double the numbers in the list
        index += 1
    print(list1)
    print(list2)
