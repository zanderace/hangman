while True:
    guess = input("Guess a letter: ")
    if len(guess) == 1 &  guess.isalpha():
        break
        
    else:
        print("Invalid letter. Please, enter a single alphabetic letter")