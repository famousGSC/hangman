import random
word_list = ["Banana", "Apple", "Kiwi","Strawberry","Blueberry"]
word=random.choice(word_list)
print(word)

def take_input():

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

take_input()