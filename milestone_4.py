import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = list(self.word)
        self.num_letters
        self.num_lives
        self.word_list
        self.list_of_guesses