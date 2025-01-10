"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.). 
"""

def is_number_prime(a): 
    if a <= 1: 
        return "The number is NOT a prime number"
    
    for number in range(2, a): 
        if a % number == 0: 
            return "The number is NOT a prime number"
    return "The number is a prime number"


try: 
    a = int(input("Enter a number: "))
except ValueError: 
    print("You need to enter a number\n")
    exit()

print(is_number_prime(a))
