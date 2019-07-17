'''
Animal Crackers: Write a function takes a two-word string
and returns True if both words begin with same letter

animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
'''

def animal_crackers(text):
    wordlist = text.lower().split()
    print(wordlist)

    first = wordlist[0]
    second = wordlist[1]

    return first[0] == second[0]

animal_crackers('Levelheaded Llama')