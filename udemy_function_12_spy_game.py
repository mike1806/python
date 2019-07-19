'''
write a function that takes in a list of integers and returns True
if it contains 007 in order
spy_game([1,2,3,7,0,0,7,5]) --> True
spy_game([1,2,5,6,3,8,0,7]) --> False

'''

def spy_game(nums):

    code = [0,0,7,'x']
    #[0,7,'x']
    #[7,'x']
    #['x'] length=1
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

spy_game([1,2,3,7,0,0,7,5])