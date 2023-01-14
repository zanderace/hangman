import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = []
        self.num_letters = 0
        self.num_lives = 0
        self.word_list = []
        self.list_of_guesses = []