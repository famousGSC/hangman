import random
word_list = ["Banana", "Apple", "Kiwi","Strawberry","Blueberry"]
# Generates a random word from the list
word=random.choice(word_list)
print(word)

def check_guess_valid():

    while True:
        try:
            guess = input("Please enter a single letter and press enter: ")
            if len(guess) != 1:
                raise ValueError("Too long")
            elif guess.isalpha() == False:
                raise ValueError("Not alphabetical")
            else:
                return guess
            break
        except ValueError:
            print("Invalid guess. Please, enter a single alphabetical character")
            continue

def check_letter_against_word():
    if guess in word:
        print(f"Good guess, {guess} is in the word!")
    else:
        print(f"Bad luck, {guess} is not in the word. Try again.")


guess=check_guess_valid()
check_letter_against_word()