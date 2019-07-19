'''
LEGB
L - local
E - enclosing
G - global
B -
'''

x = 50

def glob():
    global x
    print(f'X is {x}')

    # Local reassaignment on global variable!
    x = 'NEW Value'
    print(f'I just locally changed global x to {x}')



glob()

