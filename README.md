# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Code Descrption

The code for this project is written in python and makes use of the random module that is imported at the start. Initially a list of 5 fruits is stored in a variable (word_list). One of the words is picked at random, using the choice function (from random module), this will be the word the user has to guess.

Two functions are defined:

### 1) check_guess(guess)
This function checks if the guess is included within the randomly selected word for the game. Prior to doing so, the guess is converted to lower case. If the guess is corrected, a message to standard output indicates that it is so. Otherwise, a message to standard outputn indicates it is not.

### 2) ask_for_input()
This function asks the user to input a guess and checks that the guess is one letter only. If it isn't, it reverts back to asking the user for their guess. If the guess is acceptable, it is then passed to the check_guess function.

