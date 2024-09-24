"""My first CQ00 exercise!"""

__author__ = "730757297"


def mimic(message: str) -> str:
    """This function will mimic the message in the form of a string"""
    return message


def main() -> None:
    """Pulls together other functions"""
    print(mimic(message=input("What is your message?")))
    return main


if __name__ == "__main__":
    main()
