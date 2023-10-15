import random
#guesses=['k','i','p','n', 'r']

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list=word_list
        self.num_lives=num_lives
        self.word=random.choice(word_list)

        self.list_of_guesses=[]

        self.word_guessed=list(self.word.lower())
        self.hidden=[i if i in self.list_of_guesses else '_' for i in self.word_guessed]

        # Number of unique letters remaining
        self.num_letters=len(set(self.word_guessed))

        

    def ask_for_input(self):
        while True:
            try:
                guess = input("Please enter a single letter and press enter: ")
                if len(guess) != 1:
                    raise ValueError("Too long")
                elif guess.isalpha() == False:
                    raise ValueError("Not alphabetical")
                elif guess in self.list_of_guesses:
                    print(f"You've already guessed {guess}, please try again")
                    continue
                else:
                    self.list_of_guesses.append(guess)
                    self.check_guess(guess)
                    return guess, self.list_of_guesses
                break # Problem is here
            except ValueError:
                print("Invalid guess. Please, enter a single alphabetical character")
                continue

    def check_guess(self,guess):
        if guess in self.word_guessed:
            print(f"Good guess, {guess} is in the word!")
            guess = guess.lower()
            for i in range(len(self.word_guessed)):
                if self.word_guessed[i] == guess:
                    self.hidden[i]=guess
            self.num_letters-=1
            print(self.hidden)

        else:
            print(f"Bad luck, {guess} is not in the word. Try again.")
            self.num_lives-=1
            print(f"You have {self.num_lives} lives remaining.")

    def play_game(self):
        print(self.hidden)
        while True:
            if self.num_lives <= 0:
                print('You lost!')
                break
            elif self.num_letters > 0:
                self.ask_for_input()
            else:
                print('You won! Congratulations!')
                break



my_hangman=Hangman(["Ontario", "Saskatchawan", "Alberta","NovaScotia","Newfoundland", "BritishColumbia", "Nunavut", "NorthwestTerritories","Yukon", "PrinceEdwardIsland", "Quebec"])
#print(my_hangman.hidden)
#print(my_hangman.num_letters)

my_hangman.play_game()
    