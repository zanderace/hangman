import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = list('_'*len(self.word))
        self.num_letters = len(set(self.word))
        self.num_lives = 0
        self.word_list = word_list
        self.list_of_guesses = []

print(Hangman(['Apple']).num_letters)