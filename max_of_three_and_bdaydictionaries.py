"""
Implement a function that takes as input three variables, and returns the largest of the three.
Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care
of for us. All you need is some variables and if statements!
"""



def max_of_three(a, b, c): 
    numbers = sorted([a, b, c], reverse=True)
    return numbers[0]

print(max_of_three(9999, 5, 15))


"""
For this exercise, we will keep track of when our friend’s birthdays are, and be able to find
that information based on their name. Create a dictionary of names and birthdays.
When you run your program it should ask the user to enter a name, and return the birthday 
of that person back to them. The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
"""

birthdays = {
        'Albert Einstein': '14/03/1879',
        'Benjamin Franklin': '17/01/1706',
        'J.R.R. Tolkien': '03/01/1892',
        'Ian McKellen': '25/05/1939',
        'Rowan Atkinson': '01/6/1955',
        'Viggo Mortensen': '20/10/1958',
        'Andrzej Sapkowski': '21/06/1948',
        'Emma Watson': '15/04/1990',
        'Nikola Tesla': '10/07/1856',
        'Nicolaus Copernicus': '19/02/1473',
        }


print("Hello, we know the birthdays of: ")
for i, (key, value) in enumerate(birthdays.items()): 
    print(str(i+1)+":", key)

choice = (input("Whose birthday date would you like to know? Write a full name: "))

print(f'{choice} was born on', birthdays[choice])
