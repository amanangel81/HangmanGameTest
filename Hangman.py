import random  # Import the random module

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

# Function to retrieve a random word from the word library
def get_random_word(filename="word_library.txt"):
    """Retrieve a random word from the word library."""
    with open(filename, "r") as file:
        words = [line.strip().lower() for line in file]
    return random.choice(words)  # Use choice from random

# Function to display the guessed letters board
#This needs to push fully not working right now
def display_guessed_letters(guessed_letters):
    """Display the guessed letters board."""
    print("Guessed Letters: " + " ".join(guessed_letters))

# Function to play hangman
def hangman(word):
    wrong = 0
    rletters = list(word)
    board = ["_"] * len(word)
    guessed_letters = []
    win = False

    print("Welcome to Hangman")

    while wrong < len(STAGES) - 1:
        print("\n")
        display_guessed_letters(guessed_letters)
        msg = "Good luck guessing: "
        char = input(msg).lower()  # Convert input to lowercase for case-insensitive comparison

        if char in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(char)

        # Modified section to handle repeating letters
        found_indices = [i for i, letter in enumerate(rletters) if letter == char]

        if found_indices:
            for index in found_indices:
                board[index] = char
                rletters[index] = '$'
        else:
            wrong += 1

        # Rest of the code remains unchanged
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(STAGES[:e]))
        print("".join(["   " + ch for ch in board]))

        if "_" not in board:
            print("Good job!!, that was easy though lol!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(STAGES[:wrong]))
        print(f"Try again fam! It was {word}.")

# Entry point of the program
if __name__ == "__main__":
    # Get a random word and start the hangman game
    random_word = get_random_word()
    hangman(random_word)
