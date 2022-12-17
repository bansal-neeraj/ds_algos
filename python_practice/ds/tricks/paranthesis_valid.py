# s = '()[{()}()]'
# s = '(((((((('
# s = '}}}}}}}}}'
# s = '()()()(){}'
s = '((()))'


def check_valid(s):
    last = len(s) -1
    my_stack = []
    braces = {
        '(':')',
        '{':'}',
        '[':']'
    }
    while last >=0:
        if s[last] not in braces:
            my_stack.append(s[last])
            last -= 1
        elif my_stack:
            x = my_stack.pop()
            if braces[s[last]] == x:
                last -= 1
            else:
                return False
        else:
            return False

    if my_stack:
        return False
    else:
        return True


print(check_valid(s))

