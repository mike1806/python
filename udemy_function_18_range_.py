'''
Write a function that checks whether a number
is in a given range (Inclusive of high and low)
'''



def ran_check(num,low,high):
    #check if num is between low and high
    if num in range(low,high+1):
        print(" %s is in the range" %str(num))
    else:
        print("The number is outside the range.")

    # boolean solution

def ran_bool(num,low,high):
    return num in range(low,high+1)
ran_bool(3,1,10)
