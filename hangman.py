import random

# List of 5 predefined words
words = ["python", "computer", "programming", "keyboard", "internet"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong guesses allowed
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman Game!")

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check if the player has guessed the whole word
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    # Take a letter from the user
    guess = input("Guess a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    # Add the guessed letter to the list
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# If maximum wrong guesses are reached
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The word was:", word)