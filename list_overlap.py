"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between
the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure this out at this point -
      we’ll get to it soon)
"""

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


duplicates = []
for number in a: 
    if number in b: 
        if number not in duplicates: 
            duplicates.append(number)
print(duplicates)


# duplicates in one line of code, set() converts list to set which eliminates duplicates,
# and then we have to convert that set again to list 
print(list(set([x for x in a if x in b])))



# list of duplicates from randomly generated lists from a given range
random_list_one = []
for i in range(101):
    random_number = random.randint(0,1000)
    random_list_one.append(random_number)


random_list_two = []
for i in range(101):
    random_number = random.randint(0,1000)
    random_list_two.append(random_number)


list_of_duplicates = []
for number in random_list_one:
    if number in random_list_two: 
            if number not in list_of_duplicates:
                list_of_duplicates.append(number)
print(sorted(list_of_duplicates))