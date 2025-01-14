# excercise 18
"""
Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns
(then prints) an appropriate boolean.

Extras:

    Use binary search.

"""

def in_or_not(a, n): 
    return n in a


list_one = list(range(10,20))

print(in_or_not(list_one, 9))
print(in_or_not(list_one, 10))
print(in_or_not(list_one, 15))
print(in_or_not(list_one, 19))
print(in_or_not(list_one, 25))



#exercise 19
"""
Take the code from the How To Decode A Website exercise
(if you didn’t do it or just want to play with some different code,
use the code from the solution), and instead of printing the results to a screen,
write the results to a txt file. 
In your code, just make up a name for the file you are saving to.

Extras:

    Ask the user to specify the name of the output file that will be saved.

"""

import requests
from bs4 import BeautifulSoup


url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

soup_nyt = BeautifulSoup(r_html, 'html.parser')
articles = soup_nyt.find_all('p', class_="indicate-hover")
titles = [title.get_text() for title in articles]

users_title = input("Name a file: ")

with open(f'{users_title}.txt', 'w') as titles_file:
    for title in titles: 
        titles_file.write(title + ' \n')


