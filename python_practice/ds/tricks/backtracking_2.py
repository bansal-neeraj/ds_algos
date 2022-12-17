"""
valid parenthesis - LC 22
"""


def valid_paren(a):
    balance = 0
    for i in a:
        if i == "(":
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            return False
    return True if balance == 0 else False


n = 4
result = []


def gen_paren(a):
    if len(a) == 2*n:
        if valid_paren(a):
            result.append("".join(a))
    else:
        a.append("(")
        gen_paren(a)
        a.pop()
        a.append(")")
        gen_paren(a)
        a.pop()


gen_paren([])

print(result)
result2 = []

def gen_paren_backtraking(a,balance):
    if balance < 0:
        return
    if len(a) == 2*n:
        if balance == 0:
            result2.append("".join(a))
    else:
        a.append("(")
        balance += 1
        gen_paren_backtraking(a, balance)
        a.pop()
        balance -= 1
        a.append(")")
        balance -= 1
        gen_paren_backtraking(a, balance)
        a.pop()
        balance =+ 1


gen_paren_backtraking([], 0)
print(result)

