import random

def randomListGenerator(lo, hi, n):
    """ This function return a list of random numbers ranging from 'lo' to 'hi' of size 'n'"""

    if type(n) != int:
        raise TypeError("The size of list you want should be of type int.")

    if n < 0:
        raise ValueError("The size of the list cannot be negative.")
   
    randomList = []

    for i in range(n):
        randomList.append(random.randint(lo, hi))
    
    return randomList

# # Test Function
size = [0, -1, True, "small", 2+1j]
# message = "The random list with size = {num} is {mylist1}."

# for size1 in size:
#     mylist = randomListGenerator(1, 100, size1)
#     print(message.format(num = size1, mylist1 = mylist))
