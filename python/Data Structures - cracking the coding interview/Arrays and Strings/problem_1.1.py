""" Implement an algorithm to determine if a string has all unique characters. What if
    you can not use additional data structures?
"""
# Implementation using set()
def has_all_unique_characters(input_str):
    character_set = set()

    # for each character in the input string if it is not in the
    # character_set then add it to the set, and if it is in the set
    # then the input string does not have all unique characters
    for char in input_str:
        if char in character_set:
            return False
        else:
            character_set.add(char)
    return True

# implementation using boolean value
# If we assume only the ascii character in the string (basic has 128 characters and
# extended has extra 128 characters with total of 256 characters)
def has_all_unique_characters_ascii(input_str):
    # create a list of size 256 to store the boolean value
    char_set = [None] * 256
    for i in range(len(input_str)):
        if char_set[ord(input_str[i])]:
            return False
        else:
            char_set[ord(input_str[i])] = True

    return True


first_test_string = 'sujan'
second_test_string = 'tamang'
third_test_string = 'myapologies'

print(has_all_unique_characters(first_test_string))         # True
print(has_all_unique_characters_ascii(second_test_string))  # False
print(has_all_unique_characters_ascii(third_test_string))   # False