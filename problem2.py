if __name__ == '__main__':
    i= 18
    total = 0
    i += 1
    total += i

    if i >= 10: total += (i==10)
    if i < 10: total += total
    
    i += 1
    if i== total:
        i += 1
        total = i
    
    print(total) # prints 19