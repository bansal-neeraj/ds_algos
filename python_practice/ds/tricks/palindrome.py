"""
to check palindrome - two pointers is an effeceint technique
"""

s = 'abccba2'


def check_plaidrome(s):
    i = 0
    j = len(s) - 1

    while i <j:
        if s[i] == s[j]:
            i += 1
            j -= 1

        else:
            return "not plaindrome"

    return "palindrome"


print(check_plaidrome(s))
