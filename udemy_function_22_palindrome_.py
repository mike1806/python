'''
Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is word, phrase, or sequence that reads the same backward as
forward, e.g., madam or nurses run.
'''

def palindrome(x):

    x = x.replace(' ','')  # This replaces all spaces " " with no space ''. (Fixes issues with strings that have spaces)

    return x == x[::-1]  # check through slicing

palindrome('nurses run')

