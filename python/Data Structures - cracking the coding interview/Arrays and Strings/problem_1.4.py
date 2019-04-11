"""
    Write a method to decide if two strings are anagrams or not.

    IndexError: list index out of range
"""
# solution using frequency histrogram
def are_anagrams(first, second):
    first_length, second_length = len(first), len(second)
    if first_length != second_length:
        return False

    frequencies = [0] * 26
    for i in range(first_length):
        frequencies[ord(first[i]) - ord('a')] += 1

    for i in range(second_length):
        if frequencies[ord(second[i])] == 0:
            return False
        frequencies[ord(second[i])] -= 1

    return True

first = 'mary'
second = 'yarmhoier'
third = 'yarm'
print(are_anagrams(first, second))
print(are_anagrams(first, third))
print()