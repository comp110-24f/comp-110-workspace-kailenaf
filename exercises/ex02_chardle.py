"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730757297"


def main() -> None:  # calls all of the functions to make the game
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) < 5:
        print("Error: Word must contain 5 characters.")
        exit()
        return word
    elif len(word) > 5:
        print("Error: Word must contain 5 characters.")
        exit()
        return word
    else:
        return word


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) < 1:
        print("Error: Character must be a single character.")
        exit()
        return letter
    elif len(letter) > 1:
        print("Error: Character must be a single character.")
        exit()
        return letter
    else:
        return letter


def contains_char(
    word: str, letter: str
) -> None:  # should not call the functions in the definition.
    print("Searching for " + str(letter) + " in " + str(word))
    count: int = 0
    if (
        letter == word[0]
    ):  # if the letter is equal to the first letter of the word and it is True, then print.
        print(str(letter) + " found at index " + str(0))
        count += 1
    if letter == word[1]:
        print(str(letter) + " found at index " + str(1))
        count += 1
    if letter == word[2]:
        print(str(letter) + " found at index " + str(2))
        count += 1
    if letter == word[3]:
        print(str(letter) + " found at index " + str(3))
        count += 1
    if letter == word[4]:
        print(str(letter) + " found at index " + str(4))
        count += 1

    if count > 0:  # Keeps up with the count of instances in the program contains_char
        print(str(count) + " instances of " + str(letter) + " found in " + str(word))
    else:
        print("No instances of " + str(letter) + " found in " + str(word))


if __name__ == "__main__":
    main()
