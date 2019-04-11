import sys

def read_numbers():
    try:
        firstNumber = float(input("Enter first number:"))
        secondNumber = float(input("Enter second number:"))
    except:
        error = sys.exc_info()[0]
        print("The error is ", error)

    return firstNumber, secondNumber

try:
    firstNumber, secondNumber = read_numbers()
    result = firstNumber / secondNumber
    print("result is {0:.2f}".format(result))

except ZeroDivisionError:
    print("The result is infinity!")

except:
    print("Some other exception")
