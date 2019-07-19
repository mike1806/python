'''
map - lambda function
'''

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve','Sally']

#output

list(map(splicer,names))

['EVEN', 'E', 'S']
