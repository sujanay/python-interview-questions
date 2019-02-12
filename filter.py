def f(x):
    return x == 1 or x % 3 == 2

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(filter(f, L)))