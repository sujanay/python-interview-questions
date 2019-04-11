"""
    ---------------------- Problem: --------------------
    A string is said to be a child of a another string if it can be formed by
    deleting 0 or more characters from the other string. Given two strings of
    equal length, what's the longest string that can be constructed such that
    it is a child of both?
    For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD.
    They can be formed by eliminating either the D or C from both strings. Note
    that we will not consider ABCD as a common child because we can't rearrange
    characters and ABCD  ABDC.
    ----------------FUNCTION DESCRIPTION---------------
    Complete the commonChild function in the editor below. It should return the
    longest string which is a common child of the input strings.
    commonChild has the following parameter(s):
    s1, s2: two equal length strings
"""
# This program does not consider the ordering of the characters in the input string

# Return char counts
def getCharCount(str):
    s1_count = {}
    for char in str:
        if char not in s1_count:
            s1_count[char] = 1
        else:
            s1_count[char] += 1
    return s1_count


# Complete the commonChild function below.
def commonChild(s1, s2):
    count = 0
    s1_count, s2_count = getCharCount(s1), getCharCount(s2)

    for char in s1_count:
        if char in s2_count:
            if s1_count[char] < s2_count[char]:
                count += s1_count[char]
            else:
                count += s2_count[char]
    return count

print(commonChild('sujanay', 'tamang'))
print(commonChild('SHINCHAN', 'NOHARAAA'))
