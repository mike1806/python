'''
LEGB [bottom to top importnce]
4. L - local
3. E - enclosing
2. G - global
1. B - built- in (function)
'''
#global
name = 'Michael'

def greet():
    #enclosing
    name = 'Mike'

    def hello():
        #local
        name = 'Michal'
        print('Hello '+name)

    hello()

greet()
