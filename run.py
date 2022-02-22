""" Import random words from the dictionary to the main .py """

import random

from dictionary import dictionary

""" Some words in the list contain a '-' or a ' ' 
    which won't work in the game so they need to 
    be skipped for a usable word"""

def get_usable_word(dictionary):
    word = random.choice(dictionary)
    while '-' in word or ' ' in word:
        word = random.choice(dictionary)

    return word


