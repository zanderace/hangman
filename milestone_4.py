import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = list('_'*len(self.word))
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        self.guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")
            if len(guess) != 1 or guess.isalpha()==False:
                print("Invalid letter. Please enter a single alphabetic character")

            elif guess in self.list_of_guesses :
                print("You already tried that letter!")

            else:
                self.check_guess(guess)

Hangman(['Apple']).ask_for_input()
