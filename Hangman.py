import random

# Constants for hangman stages
STAGES = [
    "",
    "________",
    "|",
    "|     |",
    "|     0",
    "|    /|\\",
    "|    / \\",
    "|"
]


def get_random_word(filename="word_library.txt"):
    """Retrieve a random word from the word library."""
    with open(filename, "r") as file:
        words = [line.strip().lower() for line in file]
    return random.choice(words)


def hangman(word):
    wrong = 0
    rletters = list(word)
    board = ["_"] * len(word)
    win = False

    print("Welcome to Hangman")

    while wrong < len(STAGES) - 1:
        print("\n")
        msg = "Good luck guessing: "
        char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print(" ".join(board))
        e = wrong + 1
        print("\n".join(STAGES[:e]))
        print("".join(["   " + ch for ch in board]))

        if "_" not in board:
            print("Good job, that was easy though!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(STAGES[:wrong]))
        print(f"Try again fam! It was {word}.")


if __name__ == "__main__":
    # Resolve the conflict by choosing one branch's version of this block
    random_word = get_random_word()
    hangman(random_word)