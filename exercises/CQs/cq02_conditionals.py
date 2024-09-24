"""Practicing with conditionals!"""

__author__ = "730757297"


def guess_a_number() -> None:
    secret: int = 7
    x = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if x == secret:
        print("You got it!")
    elif x < 7:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
