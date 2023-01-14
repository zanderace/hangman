import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = None
        self.num_letters = None
        self.num_lives = None
        self.word_list = None
        self.list_of_guesses = None