"""My Forth Exercise Called Utils!"""

__author__ = "730757297"


def all(list1: list[int], num: int) -> bool:
    for item in list1:
        if item != num:
            return False
    return True


def max(list2: list[int]) -> int:
    if len(list2) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        placeholder = list2[0]
        for item in list2:
            if (
                item > placeholder
            ):  # if the item is greater than placeholder it will go through the entire list and return the highest number
                placeholder = item
    return placeholder


def is_equal(list3: list[int], list4: list[int]) -> bool:
    if len(list3) != len(list4):
        exit()  # if the length of list 3 does not equal the length of list 4, then exit the function
    else:
        if (
            list3 != list4
        ):  # if the lengeths of both lists are equal, then go through the lists
            return False
    return True


def extend(a: list[int], b: list[int]) -> None:
    c: list[int]
    for i in b:
        a.append(i)
    print(a)
