"""A file named coordinates under CQ04!"""

__author__ = "730757297"


def get_coords(xs: str, ys: str) -> None:

    index: int = 0  # print the pairs of both strings
    while index < len(xs):
        index: int = 0
        index += 1
        print(xs)
        while index < len(ys):  # while loop nested within another while loop
            index += 1
            print(xs, ys)
