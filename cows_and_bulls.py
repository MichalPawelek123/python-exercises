"""
Create a program that will play the “cows and bulls” game with the user.
 The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a “bull”. 
For every digit the user guessed correctly in the wrong place is a “cow.”
Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout the game and tell
the user at the end.
"""

import random

# generate a random 4 digit number for the game
def get_random_number():    
    random_number = [str(random.randint(1, 9)) for _ in range(4)]
    number =''.join(random_number)
    return int(number)

# return the message telling which letters are in the number but in the wrong place(cow) 
# or letters that are in the number and the right place(bulls)
def cow_or_bull(guess, number, bulls): 
    guess = str(guess)
    number = str(number)
    cow_num = 0
    bull_num = 0

    for i in range(len(guess)):
        if guess[i] == number[i]: 
            bull_num +=1
        elif guess[i] in number: 
            cow_num += 1

    message = f"You get {bull_num} bulls and {cow_num} cows!"
    return {'bull_num': bull_num, 'message': message}


def main(): 
    print("Game called cows and bulls, guess the 4 digit number! \n Each time i will tell you"
          " if you guessed correctly one of the numbers but in the wrong place and you will get"
           " a cow. If you guess correctly both the number and its placement - you will get a bull")
    
    random_number = get_random_number()
    tries = 0
    most_bulls = 0
    best_guess = ""
    
    while True: 
        user_guess = None

        # continue the game only if user types in the valid 4 digit number
        while user_guess is None: 
            try: 
                user_input = input("Guess a number: ")
            except ValueError: 
                print("You need to enter a valid 4 digit number")
                continue
            if len(user_input) != 4: 
                print("You need to enter a valid 4 digit number")
                continue
            user_guess = int(user_input)

        tries+=1 
        returned_round_info = cow_or_bull(user_guess, random_number, most_bulls)
        print(returned_round_info['message'])

        if user_guess == random_number: 
            print(f"\nWell done, {user_guess} was the hidden number!\n"
                   f"It took {tries} tries to find it")
            break
        
        if returned_round_info['bull_num'] > most_bulls:
            most_bulls = returned_round_info['bull_num']
            best_guess = user_guess

            print( "\n best guess so far: "
                    f"number {best_guess} with {most_bulls} bulls")
            

main()