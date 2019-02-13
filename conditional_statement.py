import sys

def timesTen(x):
    return x*10

def main():

    myInt, yourInt = 4, -2

    if(timesTen(myInt)) <= timesTen(yourInt):
        print(1)
    elif timesTen(myInt) >= timesTen(timesTen(yourInt)):
        print(2)
    else:
        print (3)

    return 0

main()  # prints 2