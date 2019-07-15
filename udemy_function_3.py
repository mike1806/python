# find out if the word "dog" is in a string

def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False

dog_check('dog ran away')

'dog' in 'dog ran away'
