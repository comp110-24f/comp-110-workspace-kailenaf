"""Practicing with While Loops!"""

__author__ = "730757297"


def num_instances(phrase: str, search_char: str) -> int:  # a function definition with two arguements
    count: int = 0
    index: int = 0
    while index < len(phrase):  # a condtion that will repeat the if else blocks
        if phrase[index] == search_char:
            count += 1
            index += 1
        else:
            index += 1

    return count


print(return)
