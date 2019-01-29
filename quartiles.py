# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
    This program returns the quartiles (Q1, Q2 & Q3) of the numbers provided.

    First the user is prompted to enter the value for 'N', the count of numbers
    the user considers to calculate the quartiles, and then the user is prompted
    to enter the numbers separated by space.
"""

# read n
n = int(input("Enter N:"))

# read n spaced numbers
arr = list(map(int, input("Enter n <space separated eg. 1 3 2 4 5> number:").split()))

def return_median(arr):
    """receives an array and returns the median and the left half and right half 
       of the median.
    """
    mid = len(arr)//2
    arr = sorted(arr)

    if len(arr) % 2: 
        med = arr[mid]
        left_half = arr[:mid]
        right_half = arr[mid+1:]
    else: 
        med = ((arr[mid-1] + arr[mid])/2)
        med = med if med % 1 else int(med)
        left_half = arr[:mid]
        right_half = arr[mid:]
    
    return [med, left_half, right_half]

[Q2, left_half, right_half] = return_median(arr)

print(return_median(left_half)[0])
print(Q2)
print(return_median(right_half)[0])