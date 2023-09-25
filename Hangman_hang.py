import random

# List of words to choose from
word_list = ["paris", "spain", "seoul", "india", "busan", "america", "poland", "london"]

# Select a random word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize game variables
display = []
for _ in range(word_length):
    display += "_"

# Hangman stages
stages = [
    """
     -----
    |     |
          |
          |
          |
          |
    """,
    """
     -----
    |     |
    O     |
          |
          |
          |
    """,
    """
     -----
    |     |
    O     |
    |     |
          |
          |
    """,
    """
     -----
    |     |
    O     |
   /|     |
          |
          |
    """,
    """
     -----
    |     |
    O     |
   /|\\    |
          |
          |
    """,
    """
     -----
    |     |
    O     |
   /|\\    |
   /      |
          |
    """,
    """
     -----
    |     |
    O     |
   /|\\    |
   / \\    |
          |
    GAME OVER!
    """
]

# Track guessed letters
guessed_letters = []

# Game loop
game_over = False
attempts = len(stages) - 1

while not game_over:
    # Display the current state of the word
    print(" ".join(display))

    # Get a guess from the player
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try again.")
        continue

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        print(f"'{guess}' is not in the word.")
        guessed_letters.append(guess)
        attempts -= 1
        print(stages[attempts])

    if "_" not in display:
        print("Congratulations! You guessed the word.")
        game_over = True
    elif attempts == 0:
        print(f"Out of attempts. The word was '{chosen_word}'.")
        game_over = True
