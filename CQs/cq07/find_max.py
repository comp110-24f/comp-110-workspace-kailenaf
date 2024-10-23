"""A file called find_max that is used for CQ07!"""

__author__ = "730757297"


def find_and_remove_max(list1: list[int]) -> int:
    if len(list1) == 0:
        return -1
    else:
        item: int = list1[0]
        i: int = 0
    for num in list1:  # for every # in list 1, if the # is > items and items = #
        if num > item:
            item = num
    while i < len(list1):
        if item == list1[i]:
            list1.pop(i)
            i -= 1
        i += 1
    return item
