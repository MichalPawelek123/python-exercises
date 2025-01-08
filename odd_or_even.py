"""
The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""


number = int(input("Pick a number: "))
check = int(input("Pick a second number: "))

if number%2: 
    print("the number is odd")
else: 
    print("the number is even")
    if number%4 == 0: 
        print("the number is also a multiple of 4!")

sum = number/check

if not sum%2: 
    print("the numbers divide evenly")

