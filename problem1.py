from __future__ import print_function

def f(n):
    return (n <= 4) <= (n <= 5)

def main():
    i = 0
    while True:
        if not f(i) or i == 1729:
            print(i)
            break
        i += 1

main()