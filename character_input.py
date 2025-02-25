"""
Create a program that asks the user to enter their name and their age. Print out a message
addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out 
the year (and therefore be out of date the next year). 

Extras:

    Add on to the previous program by asking the user for another number and printing out that many
    copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. 
    (Hint: the string "\n is the same as pressing the ENTER button)

"""
import datetime

try: 
    name = input("Whats your name: ")
    age = int(input("How old are you: "))

    year_to_be_hundrer = datetime.date.today().year + (100-age)

    print(f'Hello {name}, you will be 100 years old in {year_to_be_hundrer}')
except ValueError: 
    print("Age cannot be a string")
    exit()
    