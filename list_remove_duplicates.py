"""
Write a program (function!) that takes a list and returns a new list that contains
all the elements of the first list minus all the duplicates.

Extras:

    Write two different functions to do this - one using a loop and constructing a list,
    and another using sets.
"""

import random

# remove duplicates using set
def remove_duplicates(a): 
    return list(set(a))


def remove_duplicates_loop(a): 
    b = []
    for n in a: 
        if n not in b:
            b.append(n)
    return sorted(b)


# random list with possible duplicates
z = [random.choice(range(20)) for i in range(20)]

print("Generated list: ", sorted(z))
print("\nRemove duplicates with set(): ",remove_duplicates(z))
print("\nRemove duplicates with for loop: ",remove_duplicates_loop(z))