""" Import random words from the dictionary to the main .py """

import random

import string

from dictionary import dictionary

""" Some words in the list contain a '-' or a ' ' 
    which won't work in the game so they need to 
    be skipped for a usable word"""

def get_usable_word(dictionary):
    word = random.choice(dictionary)
    while '-' in word or ' ' in word:
        word = random.choice(dictionary)

    return word

""" For correctly/ incorrectly guessed letters and valid letters.
    And a loop to prevent the use of repeat of already guessed letters """

def hang_man():
    word = get_usable_word(dictionary)
    correct_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    played_letters = set()

    user_guess = input('Guess Your Letter: ').upper()
    if user_guess in alphabet - played_letters:
        played_letters.add(user_guess)
        if user_guess in correct_letters:
            correct_letters.remove(user_guess)

    

player_input  = input('Guess Here: ')
print(player_input)


