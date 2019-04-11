def rev_str(str):
    rev_string =''

    for i in range(len(str)):
        rev_string += str[-(i+1)]

    return rev_string

print(rev_str('panda'))