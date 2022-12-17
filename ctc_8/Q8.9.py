"""check for valid parentheses"""


def valid_paren(p,my_stack):
    if len(p) == 0:
        if my_stack:
            return False
        else:
            return True

    if p[-1] == ')':
        my_stack.append(p[-1])
        return valid_paren(p[:-1], my_stack)
    else:
        if my_stack:
            my_stack.pop()
            return valid_paren(p[:-1], my_stack)
        else:
            return False


# parens = '((()))'
# parens = '(()())'
# parens = '(())()'
# parens = '()(())'
parens = '()()()'
my_stack = []

print(valid_paren(parens, my_stack))



