import random

randomList = random.sample(range(1,26000000), 10000000)

print("Random List:", randomList)

num = int(input("Enter a number to search in the list:"))

lo, hi = 0, 9

randomList.sort()

print("Sorted list:", randomList)

fount = False

while lo < hi:
    mid = (lo + hi)//2

    if randomList[mid] == num: 
        # print("Your number is in the list", mid)
        # break
        found = True
        break

    elif randomList[mid] < num:
        lo = mid
        # print("Not in the list HIGH")
    else: 
        hi = mid
        # print("Not in the list LOW")

if found: print("Your number is in the list!!")
else: print("Not in the List!!!")

    