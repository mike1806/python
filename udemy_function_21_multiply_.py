'''
Write a Python function to multiply all the numbers in a list.
Sample List : [1, 2, 3, -4]
Expected Output : -24
'''

def multiply(num):
    total = num[0]
    for x in num:
        total *= x
    print(total)
multiply([1, 6, 3, -25])
