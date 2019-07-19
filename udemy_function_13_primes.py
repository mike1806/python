'''
Write a function that returns the number of prime numbers that exist up to
and including a given number
By convention we ll treat 9 and 1 as not prime
'''

def count_prime(num):
    #check for 0 or 1 input
    if num < 2:
        return 0

    #2 or greater

    #store our prime numbers
    primes = [2]
    # counter going up to the input num
    x = 3
    # x is going through every number up to input num
    while x <= num:
        for y in range(3,x,2)
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    retun len(primes)