"""A program to Plan a Tea Party!"""

__author__: str = "730757297"


def main_planner(
    guests: int,
) -> (
    None
):  # calling all functions by using the parameter of guests, and using guest equals people to call other functions
    """Bringing these functions together in a "main planner" function that calls each and produces printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print(
        "Treats: " + str(treats(people=guests))
    )  # calling treats to get the number of treats
    print(
        "Cost: $"
        + str(
            float(
                cost(
                    tea_count=tea_bags(people=guests), treat_count=treats(people=guests)
                )
            )
        )
    )


def tea_bags(people: int) -> int:
    """A function to compute the number of tea bags needed based on the number of guests."""
    return people * 2


def treats(people: int) -> int:
    """A function to compute the number of treats needed based on the number of teas guests are expecting to drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """A function to compute the cost of the tea bags and the treats combined."""
    return float(tea_count * 0.50 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
