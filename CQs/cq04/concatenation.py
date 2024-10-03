"""A file named concatenation under CQ04!"""

__author__ = "730757297"


def main() -> (
    None
):  # surpressing the import call, but not the actual calling of concat function
    concat(word1, word2)


def concat(word1: str, word2: str) -> str:
    return word1 + word2


word1: str = "happy"
word2: str = "tuesday"


if __name__ == "__main__":
    main()
    print(concat(word1, word2))
