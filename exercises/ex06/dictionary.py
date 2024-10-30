"""A file called dictionary that is used for EX06!"""

__author__ = "730757297"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    inverted_dict = {}  # new dictionary

    for key, value in dict1.items():  # for every key value pair in dict 1
        if value in inverted_dict:  # if the values are in the inverted dict
            raise KeyError(
                f"There are duplicate values found: {value}"
            )  # raise the error
        inverted_dict[value] = key

    return inverted_dict


def favorite_color(dict2: dict[str, str]) -> str:
    count_color = {}
    count_order = {}

    for name, color in dict2.items():  # for every name color pair in dict2
        if color not in count_color:  # if the color is not in the color counter
            count_color[color] = 0
            count_order[color] = name

        count_color[color] += 1  # increase by 1

    popular_color = None
    max_count = 0

    for color, count in count_color.items():
        if count > max_count:
            popular_color = color
            max_count = count

    return popular_color


def count(value: list[str]) -> dict[str, int]:
    result_dict = {}

    for item in value:  # for every item in value
        if item in result_dict:
            result_dict[item] += 1  # increase by 1
        else:
            result_dict[item] = 1

    return result_dict


def alphabetizer(word: list[str]) -> dict[str, list[str]]:
    final_dict = {}  # new dict
    for words in word:
        first_letter = words[0].lower()  # .lower will give the lower case

        if first_letter not in final_dict:
            final_dict[first_letter] = []

        final_dict[first_letter].append(words)  # add to the dict

    return final_dict


def update_attendance(
    attendance_dict: dict[str, list[str]], day: str, student: str
) -> None:
    if day not in attendance_dict:  # if the day is not in the attendance dict
        attendance_dict[day] = []

    attendance_dict[day].append(student)
