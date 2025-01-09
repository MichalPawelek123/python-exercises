"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out
    """

import random


user_input = ""
tries = 1

while True: 
    print("\n\n Guessing game. Guess a number between 1 and 9 and I will tell you if thats the number"
          "I though about\n")
    random_number = random.randint(1,9)
    user_guess = -1

    while user_guess != random_number: 
        user_guess = int(input("Your guess: "))

        if user_guess == random_number: 
            print(f"Thats right, the number I thought about is {user_guess}, you won! \n"
                f"Number of tries: {tries}")
            user_input = input(""" Type "exit" if you want to quite the game, else press any button and press ENTER to continue """.lower())
            if user_input == "exit":
                exit()
        else: 
            tries+=1
            if user_guess > random_number: 
                print("Try a lower number")
            else: 
                print("Try a higher number")