import random
#guesses=['k','i','p','n', 'r']

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list=word_list
        self.num_lives=num_lives
        self.word=random.choice(word_list)

        self.word_guessed=list(self.word.lower())
        self.hidden=['_' if i in guesses else i for i in self.word_guessed]

        # Number of unique letters remaining
        self.num_letters=len(set(self.hidden))-1 # -1 is so you don't count the '_' character

        self.list_of_guesses=[]

    def ask_for_input():

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

    def check_guess(guess):
        if guess in word:
            print(f"Good guess, {guess} is in the word!")
        else:
            print(f"Bad luck, {guess} is not in the word. Try again.")


my_hangman=Hangman(["Banana", "Apple", "Kiwi","Strawberry","Blueberry"])
print(my_hangman.hidden)
print(my_hangman.num_letters)
    