"""
Write a password generator in Python. Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new
password. Include your run-time code in a main method.
"""

import string
import random

def password_generator(n=15): 
    password = []
    numbers = string.digits
    letters = string.ascii_lowercase
    letters_uppercase = string.ascii_uppercase
    special_signs = "!@#$%^&*()-_+=[]{}<>?"

    dict_of_lists = {
        1 : numbers, 
        2 : letters,
        3 : letters_uppercase,
        4 : special_signs
    }

    for _ in range(n): 
        list_from_dict = dict_of_lists[random.randint(1,4)]
        password.append(random.choice(list_from_dict))       
    return ''.join(password)

        
def main(): 
    while True: 
        try: 
            n = int(input("Enter password length: "))
            break
        except ValueError: 
            print(" You need to enter an integer")

    print("Generated password: ", password_generator(n))


main()
