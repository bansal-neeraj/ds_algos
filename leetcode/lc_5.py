def longestPalindrome(s: str) -> str:
    possible_palindrome = []
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            possible_palindrome.append((i, i + 2))
        if s[i] == s[i + 1]:
            possible_palindrome.append((i, i + 1))
    i += 1
    if s[i] == s[i + 1]:
        possible_palindrome.append((i, i + 1))

    print(possible_palindrome)

    left, right = 0, 0
    ans = (0, 0)
    for i in possible_palindrome:
        left = i[0]
        right = i[1]

        while left >= 0 and right <= len(s) - 1:
            if s[left] == s[right]:
                if ans[1] - ans[0] < right - left:
                    ans = (left, right)
                left -= 1
                right += 1
            else:

                break

    print(ans)
    return s[ans[0]:ans[1] + 1]


print(longestPalindrome('babad'))
# print(longestPalindrome('cbbd'))