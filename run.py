

import random

import string

from dictionary import dictionary

# Usable words - remove words from dictionary that are not valid such as '-' and ' ' 

def get_usable_word(dictionary):
    word = random.choice(dictionary)
    while '-' in word or ' ' in word:
        word = random.choice(dictionary)

    return word.upper()

# Adding all possible outcomes such as invalid guesses, correct guesses and already guessed letters   

def game():
    word = get_usable_word(dictionary)
    correct_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    played_letters = set()

#Added in Error messages when invalid or already guessed letters are entered. This is looped so the game moves smoothly and another attempt is made

    chances = 6

    while len(correct_letters) > 0 and chances > 0:
        print('You have' , chances, 'chances left. ' 'Attempted Letters: ', ' '.join(played_letters))

        word_list = [letter if letter in played_letters else '-' for letter in word]
        print('Word: ', ''.join(word_list))

        user_guess = input('Guess Your Letter: ').upper()
        if user_guess in alphabet - played_letters:
            played_letters.add(user_guess)
            if user_guess in correct_letters:
                correct_letters.remove(user_guess)

            else:
                chances = chances - 1   #Takes away a life when incorrect
                print('This is not in the word!/n')

        elif user_guess in played_letters:
            print('You Have Already Guessed This Letter! Try Again...')

        else:
            print('Invalid Guess! Please Try Again')

    if chances == 0:
        print('You Failed! The word was', word)
    else:
        print('You Guessed the word', word, '!!') 

game()


