import random
WORDS = ["python", "hangman", "internship", "keyboard", "variable"]
MAX_ATTEMPTS = 6
def choose_word():
    """Randomly pick a word from the list."""
    return random.choice(WORDS)
def display_progress(word, guessed_letters):
    """
    Build a string showing guessed letters in their correct
    position, and underscores for letters not yet guessed.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()
def play_hangman():
    """Main game loop for a single round of Hangman."""
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {MAX_ATTEMPTS} incorrect guesses allowed.\n")
    while wrong_guesses < MAX_ATTEMPTS:
        print("Word: " + display_progress(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{MAX_ATTEMPTS}")
        if guessed_letters:
            print("Guessed letters: " + ", ".join(guessed_letters))
        guess = input("Guess a letter: ").lower().strip()        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another.\n")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print("Good guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")       
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            return   
    print(f"Game over! You've used all {MAX_ATTEMPTS} incorrect guesses.")
    print(f"The word was: {word}")
def main():    
    while True:
        play_hangman()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break
        print()
if __name__ == "__main__":
    main()
