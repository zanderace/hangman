import random 

#list of fruits that guess word is picked from
word_list = ['apple','pear','grapefruit','banana','kiwi']

# select a random fruit from the list and assign to word
word = random.choice(word_list)

#print(word)

#check guess is one letter
while True:
    guess = input("Guess a letter: ")
    if len(guess) == 1 &  guess.isalpha():
        break
        
    else:
        print("Invalid letter. Please, enter a single alphabetic letter")

#check if guess is correct
if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry , {guess} is not in the word. Try again.")