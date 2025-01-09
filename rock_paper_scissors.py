"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, and ask if the players 
want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

*I modified it to play against PC
"""

import random
import time

OPTIONS = {
    1 : "ROCK",
    2 : "PAPER",
    3 : "SCISSORS",
    4 : "EXIT",
 }

pick = 0
while True: 

    for key, value in OPTIONS.items(): 
        print(key, "--->" ,value, "\n")

    user_pick = -1
    while user_pick < 1 or user_pick > 4: 
        try:            
            user_pick = int(input("Pick your weapon or press 4 to EXIT: \n",))
            if user_pick == 4:
                print("Thanks for playing! Gooodbye")
                exit()
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
        if user_pick < 0 or user_pick > 4: 
            print("You need to pick a proper value to continue... \n")
            
    
    computer_pick = random.randint(1,3)

    print(f"You picked {OPTIONS[user_pick]}\n")
    time.sleep(1)
    print(f"COMPUTER picked {OPTIONS[computer_pick]}\n")
    time.sleep(1)
    
    if user_pick == computer_pick: 
        print(f"You both picked {OPTIONS[user_pick]}, it's a DRAW!")

    elif user_pick == 1 and computer_pick == 2: 
        print("YOU LOST! Rock against paper!")
    elif user_pick == 1 and computer_pick == 3:
        print("YOU WON! Rock against scissors!")
    elif user_pick == 2 and computer_pick == 1: 
        print("YOU WON! Paper against rock!")
    elif user_pick == 2 and computer_pick == 3: 
        print("YOU LOST! paper against scissiors!")
    elif user_pick == 3 and computer_pick == 1: 
        print("YOU LOST! Scissors against rock!")
    elif user_pick == 3 and computer_pick == 2: 
        print("YOU WON! Scissors against paper!")
    
    print("\n"*5)
    new_game = input("Press Y if you want to START a new game, press any other button if you want to QUIT: \n").lower()
    if new_game != "y": 
        print("Thanks for playing! Gooodbye")
        break



    

