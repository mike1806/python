'''
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''

def unique_list(u):
        # possible to use list(set())
    n = []
    for a in u:
        if a not in n:
            n.append(a)
    return n
unique_list(  [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]  )
