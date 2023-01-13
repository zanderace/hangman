import random 

#list of fruits that guess word is picked from
word_list = ['apple','pear','grapefruit','banana','kiwi']

# select a random fruit from the list and assign to word
word = random.choice(word_list)

#print(word)

#function to check if guess is correct
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry , {guess} is not in the word. Try again.")

#function to check guess is one letter
def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 &  guess.isalpha():
            break
            
        else:
            print("Invalid letter. Please, enter a single alphabetic letter")
    check_guess(guess)

ask_for_input()