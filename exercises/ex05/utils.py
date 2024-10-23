"""A file called utils that is used for EX05!"""

__author__ = "730757297"


def only_evens(list1: list[int]) -> int:
    even_nums: list[int] = []
    for number in list1:
        if number % 2 == 0:  # if the number is even
            even_nums.append(number)
    return even_nums


def sub(list2: list[int], num1: int, num2: int):
    if len(list2) == 0 or num1 >= len(list2) or num2 <= 0:  # if there is an empty list
        return []
    if num1 < 0:  # if the start index is negative
        num1 = 0
    if num2 > len(list2):  # if the end index is greater than the list length
        num2 = len(list2)
    return list2[num1:num2]


def add_at_index(list3: list[int], num3: int, num4: int) -> None:
    if num4 < 0 or num4 > len(
        list3
    ):  # check if the index is out of range and will raise an error
        raise IndexError("Index is out of bounds for the input list")
    list3.append(num3)  # append the elements from list 3
    for i in range(len(list3) - 1, num4, -1):
        list3[i] = list3[i - 1]
    list3[num4] = num3
