import random
from tkinter import *
from tkinter import ttk

root = Tk()

label_title = ttk.Label(root, text="H-A-N-G-M-A-N")
label_title.grid(row=0, column=0, columnspan=5)
label_title.pack()

label_maskedword = ttk.Label(root, text="_ _ _ _ _")
label_maskedword.grid(row=3, column=1, columnspan=3)
label_maskedword.pack

label_misses = ttk.Label(root, text="misses go here")
label_misses.grid(row=4, column=1, columnspan=3)
label_misses.pack()

label_guess = ttk.Label(root, text="Guess: ")
label_guess.grid(row=5, column=0)
label_guess.pack()


#textbox = ttk.T

button_guess = ttk.Button(root, text="Guess")
button_guess.grid(row=5, column=3)

list_of_words = ("psych",
                 "rhubarb",
                 "broadside",
                 "punctual",
                 "television")

new_game = True

while new_game:
    word_to_guess = list_of_words[random.randint(0, 4)]
    misses = ''
    number_of_guesses_remaining = 6
    masked_word = "_" * len(word_to_guess)
    masked_word_as_list = list(masked_word)
    while number_of_guesses_remaining >= 0:
        print("Word:\t" + str.upper(' '.join((letter for letter in masked_word))))
        print("Misses: " + misses)
        if number_of_guesses_remaining == 0:
            print()
            print("You ran out of guesses!")
            print("The answer was: " + str.upper(word_to_guess))
            print()
            break
        guess = str.lower(input("Guess:\t"))
        if guess in word_to_guess:
              for ind, letter in enumerate(word_to_guess):
                if guess == letter:
                    masked_word_as_list[ind] = (guess)
                elif not masked_word_as_list[ind] == '_ ':
                    continue
                else:
                    masked_word_as_list[ind] = "_ "
              masked_word = ''.join(masked_word_as_list)
              if masked_word == word_to_guess:
                  print()
                  print("Word:\t" + str.upper(' '.join((letter for letter in masked_word))))
                  print("Misses: " + misses)
                  print()
                  print("You guessed the correct word!")
                  print()
                  break
        else:
            if misses == '':
                misses = str.upper(guess)
            else:
                misses += " " + str.upper(guess)
            number_of_guesses_remaining -=1
        print()

    print("Would you like to play again?")
    new_game_prompt = str.lower(input("(Y/N): "))

    if new_game_prompt == 'y':
        new_game = True
    else:
        new_game = False