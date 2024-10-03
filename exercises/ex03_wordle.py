"""Exercise three: Wordle!"""

__author__ = "730757297"


def input_guess(secret_word_len: int) -> str:
    user_guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(user_guess) != secret_word_len:
        user_guess: str = input(f"That wasn't {secret_word_len} chars! Try again: ")
    print(user_guess)
    return user_guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Function to test each index of first parameter to match the second parameter"""
    assert len(char_guess) == 1
    index: int = 0
    while len(secret_word) > index:
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


WHITE_BOX: str = "\U00002B1C"  # allows the emojis to be defined and colored
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(user_guess: str, secret_word: str) -> str:
    """Using different colored emojis to indicate if a character is in the correct position"""
    assert len(user_guess) == len(secret_word)

    result = ""
    index = 0

    while index < len(user_guess):
        if user_guess[index] == secret_word[index]:
            result += GREEN_BOX  # allows the emojis to be used in the function
        elif contains_char(
            secret_word, user_guess[index]
        ):  # must use elif to incorporate contains_char function
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


# main function to run the whole program
def main(secret_word: str) -> None:
    """The entrypoint of the program and main game loop."""
    max_turns: int = 6
    current_turn: int = 1
    has_won = False

    while current_turn <= max_turns and not has_won:
        print(
            f"=== Turn {current_turn}/{max_turns} ==="
        )  # will print the statement with the current turn and max turn in fraction
        guess_word = input_guess(
            len(secret_word)
        )  # input guess must be the length of the secret word
        result = emojified(guess_word, secret_word)
        print(result)
        if guess_word == secret_word:
            has_won = True
        else:
            current_turn += 1

    if has_won:
        print(
            f"You won in {current_turn}/{max_turns} turns!"
        )  # print if the player has won the game
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret_word="codes")
