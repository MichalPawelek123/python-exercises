"""
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. 

For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.
"""

# split() without arguments splits a given string on whitespaces, 
# [::-1] reverses the given list, in this case a list of words
def reverse_string(s): 
    return s.split()[::-1]


print(reverse_string("My name is Michael"))