import random
word_list = ["Banana", "Apple", "Kiwi","Strawberry","Blueberry"]
# Generates a random word from the list
word=random.choice(word_list)
#print(word)

def input_letter_guess():

    while True:
        try:
            guess = input("Please enter a single letter and press enter: ")
            if len(guess) != 1:
                raise ValueError("Too long")
            else:
                return guess
            break
        except ValueError:
            print("Oops, not a single letter. Please try again.")
            continue

input_letter_guess()