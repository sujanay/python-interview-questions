"""check if the two string are anagrams of each other"""
"""
    Method-1:
    This method utilizes the fact that the anagram strings, when
    sorted,  will be equal when testing using string equality operator
"""
def Is_Anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    str1_sorted, str2_sorted = sorted(str1), sorted(str2)
    return str1_sorted == str2_sorted

print(Is_Anagram('hello', 'billion'))
print(Is_Anagram('mary', 'yarm'))
print(Is_Anagram('table', 'balet'))