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

""" For correctly/ incorrectly guessed letters and valid letters """

def hang_man():
    word = get_usable_word(dictionary)      """ Get from the above usable words """
    correct_letters = set(word)             """ Correctly guessed letters """  
    alphabet = set(string.ascii_uppercase)  """ Alphabet all uppercase so no errors """
    played_letters = set()                  """ Already played letters """


