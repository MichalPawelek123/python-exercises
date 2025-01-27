"""
This exercise is Part 1 of 3 of the Hangman exercise series.

In this exercise, the task is to write a function that picks a random word from a list of words
from the SOWPODS dictionary. 
Download this file(http://norvig.com/ngrams/sowpods.txt) and save it in the same directory
as your Python code.

This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble
tournaments. Each line in the file contains a single word.

"""

import random


def pick_a_word(file_name): 
    line_number = random.randint(1, 267751)
    interation_number = 0
    words = []

    with open(f'{file_name}', 'r') as f: 
        line = f.readline()
        while interation_number < line_number: 
            line = f.readline()
            words.append(line)
            interation_number+=1
    return words[-1]


print(pick_a_word('list_of_words.txt'))


#2nd solution
def pick_a_word2(file_name): 
    with open(f'{file_name}', 'r') as f: 
        lines = f.readlines()
        number = random.randint(0, len(lines))
        return lines[number]
    
print("Word: ", pick_a_word2('list_of_words.txt'))