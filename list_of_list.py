from __future__ import print_function

def f(lst_of_lst):
    lst_of_lst[0] = lst_of_lst[0][1:]

def main():
    lst = [2, 4, 6, 8]
    p = [lst]
    f(p)
    ret = p[0][0]
    print(ret)

main()