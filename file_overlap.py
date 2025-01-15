"""
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
One .txt file has a list of all prime numbers under 1000, and the other .txt file has
a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number.
And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
The explanation is easier with an example, which I will describe below.)
"""

# prime_numbers.txt : https://www.practicepython.org/assets/primenumbers.txt
prime_numbers = []
with open('prime_numbers.txt', 'r') as f: 
    line = f.readline()
    while line: 
        line = int(line.strip())
        prime_numbers.append(line)
        line = f.readline()

# happy_numbers.txt : https://www.practicepython.org/assets/happynumbers.txt
happy_numbers = []
with open('happy_numbers.txt', 'r') as f2: 
    line = f2.readline()
    while line: 
        line = int(line.strip())
        happy_numbers.append(line)
        line = f2.readline()

overlaping = [n for n in prime_numbers if n in happy_numbers]
print(overlaping)