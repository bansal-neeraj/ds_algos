"""
check if two strings are anagram of each other
"""

from collections import Counter

s1 = 'listen'
s2 = 'silent'
# s1 = 'dad'
# s2 = 'bad'


def check_anagram(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)

    if c1 == c2:
        return True
    else:
        return False


x = check_anagram(s1,s2)
print(x)