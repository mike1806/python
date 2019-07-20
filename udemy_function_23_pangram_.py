'''
Write a Python function to check whether a string is pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

'''

import string

def ispangram(str1, alphabet=string.ascii_lowercase):

    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

ispangram("The quick brown fox jumps over the lazy dog")

print(ispangram("Im wyżej wzlatujemy, tym mniejsi wydajemy się tym, którzy nie potrafią latać"))