"""
    find the number of characters that must be removed from two strings
    to make them anagram
    Example:
        Given two strings: hello & billion, we can remove 'he' from 'hello' and
        'biin' from billion so that they are anagrams. Therefore the total number
        of characters to be removed is 2 (he) + 4 (biin) = 6.
"""
def Anagram_Solver(str1, str2):
    """ returns the number of characters to be removed"""
    count = 0
    str1_char_count = {}
    str2_char_count = {}

    # compute character counts of str1
    for char in str1:
        if char not in str1_char_count:
            str1_char_count[char] = 1
        else: str1_char_count[char] += 1

    # compute character counts of str2
    for char in str2:
        if char not in str2_char_count:
            str2_char_count[char] = 1
        else: str2_char_count[char] += 1

    # if the char in str1 is not in str2,
    # increase the counter
    for char in str1_char_count:
        if char not in str2_char_count:
            count += str1_char_count[char]

    # finally, loop through the charcter counts
    # str2 and increment the counter by the difference
    # if the char is in both str1 and str2 else, increase
    # the counter with the unique character count of str2
    for char in str2_char_count:
        if char not in str1_char_count:
            count += str2_char_count[char]
        else: count += abs(str1_char_count[char] - str2_char_count[char])

    return count

first = 'mary'
second = 'yarmhoier'
result = Anagram_Solver(first, second)

print(result) # 5 