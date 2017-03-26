import random

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
        print("Word:\t" + str.upper(' '.join(letter for letter in masked_word)))
        print("Misses: " + misses)
        if number_of_guesses_remaining == 0:
            print()
            print("You ran out of guesses!")
            print("The answer was: " + str.upper(word_to_guess))
            print()
            break
        guess = str.lower(raw_input("Guess:\t"))
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
    new_game_prompt = str.lower(raw_input("(Y/N): "))

    if new_game_prompt == 'y':
        new_game = True
    else:
        new_game = False
        