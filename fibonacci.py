"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. Make sure to ask the user to
enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

def fib(n): 
    a = 0
    b = 1
    iteration = 0

    while iteration < n: 
        print(b)
        a, b = b, a+b
        iteration += 1
    

fib_num = int(input("How many fibonacci numbers do you want to generate: "))
fib(fib_num)