"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""
import random

a = [5, 10, 15, 20, 25]

def first_and_last(list_of_nums):
    return list([list_of_nums[0], list_of_nums[-1]])

print(a)
print(first_and_last(a), "\n")

# example on randomly generated list
rand_list = sorted(random.sample(range(100), 10))
print(rand_list)
print(first_and_last(rand_list))