while True:
    guess = input("Guess a letter: ")
    try:
        len(guess) == 1 &  guess.isalpha()
        break
    except:
        print("Invalid letter. Please, enter a single alphabetic letter")