import random 

word_list = ['apple','pear','grapefruit','banana','kiwi']
#print(word_list)

word = random.choice(word_list)
#print(word)

guess = input('Enter a single letter: ')

if len(guess) == 1 &  guess.isalpha():
    print("Good guess!")
else:
    print("Oops! This is not a valid input.")