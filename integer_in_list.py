# Write a function which takes as input a sorted list of integers (from the smallest to the largest) and
# an integer, it returns True if the integer is in the list, False if not.
import time

mylist = [i+1 for i in range(250000000)]

def isInTheList(mylist, num):

    if mylist[-1] < num: return False 

    hi = mylist[-1]
    lo = mylist[0]
    # print("hi:", hi)
    # print("lo:", lo)

    while hi > lo:
        mid = (hi + lo)//2
        if mylist[mid] == num: return True
        elif mylist[mid] > num: hi = mid
        else: lo = mid
    
    return False

start = time.time()
print(isInTheList(mylist, 2))
finish = time.time()
print("start:", start)
print("finish:", finish)
print(f"it took {finish - start} seconds!")