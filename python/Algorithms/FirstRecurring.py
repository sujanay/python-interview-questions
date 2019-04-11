def First_Recurring(str1):
    my_coll = set()

    for char in str1:
        if char in my_coll: return char
        else: my_coll.add(char)

str1 = 'abcdbed'
# str1 = 'abcdcert'

print(First_Recurring(str1))