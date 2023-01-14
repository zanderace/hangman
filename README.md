# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Code Descrption

The code for this project is written in python and makes use of the random module that is imported at the start. Initially a list of 5 fruits is stored in a variable (word_list). One of the words is picked at random, using the choice function (from random module), this will be the word the user has to guess.

## Class defintion

The Hangman class is defined with the following attributes:
word - secret word picked at random from the input word list
word_guessed - A list of letters of same length as word, initialized as underscores. This is then updated with correct guesses.
num_letters - number of unique letters in the word
num_lives - number of player lives. Default is 5
word_list - list of words that the game picks from
list_of_guesses - list of guessed letters


Two functions are defined:

### :zap: 1) check_guess(guess) :zap:
This function checks if the guess is included within the randomly selected word for the game. Prior to doing so, the guess is converted to lower case. If the guess is corrected, a message to standard output indicates that it is so. Otherwise, a message to standard outputn indicates it is not. 

### :zap: 2) ask_for_input() :zap:
This function asks the user to input a guess and checks that the guess is one letter only. If it isn't, it reverts back to asking the user for their guess. If the guess is acceptable, it is then passed to the check_guess function.

