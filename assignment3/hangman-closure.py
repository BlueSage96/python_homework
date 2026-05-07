#Task 4
def make_hangman(secret_word):
    guesses = []
    def hangman_closure(guess):
        guesses.append(guess) #store guessed letter
        final_guess = ""
        #build the display word
        for s in secret_word:
            if s in guesses:
                final_guess += s
            else:
                final_guess += "_"
        print(f"Word: {final_guess}")
        #check if word's fully guessed
        if final_guess == secret_word:
            return True
        return False   
    return hangman_closure

# game setup
secret = input("Enter the secret word: ")
game = make_hangman(secret)

# game loop
while True:
    guess = input("Guess a letter: ")
    if game(guess):
        print("You guessed the word!")
        break
        