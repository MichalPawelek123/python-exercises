"""
Given a .txt file that has a list of a bunch of names, count how many of each name there are in 
the file, and print out the results to the screen. 

Extra:

Instead of using the .txt file from above (or instead of, if you want the challenge),
take this .txt file, and count how many of each “category” of each image there are. 
This text file is actually a list of files corresponding to the SUN database scene recognition
database, and lists the file directory hierarchy for the images. Once you take a look at the
first line or two of the file, it will be clear which part represents the scene category. 
To do this, you’re going to have to remember a bit about string parsing in Python 3. 
I talked a little bit about it in this post.
"""

# count names in a given file
# file url: https://www.practicepython.org/assets/nameslist.txt

counter_dict = {}

with open('names.txt', 'r') as f: 
    line = f.readline()
    while line: 
        line = line.strip()
        if line in counter_dict:
            counter_dict[line] += 1
        else: 
            counter_dict[line] = 1
        line = f.readline()

print(counter_dict)


# Extra

# file url: https://www.practicepython.org/assets/Training_01.txt
categories = {}
with open('db_text.txt', 'r') as f2: 
    line = f2.readline()
    while line: 
        line = line.split('/')
        category = line[2]
        if category in categories:
            categories[category] += 1
        else: 
            categories[category] = 1
        line = f2.readline()

print(categories)
