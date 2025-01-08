"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""

user_input = input("Type a word to check if its a palindrome or not: ")

if list(user_input) == list(reversed(user_input)): 
    print("the word is a palindrome")
else: 
    print("the word isn't a palindrome")
