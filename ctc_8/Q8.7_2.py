s1 = 'abcdef'


def all_perm(s):
    if len(s) == 2:
        return [s, s[1]+s[0]]
    r = all_perm(s[1:])
    new_r = []
    for i in r:
        for j in range(len(i)+1):
            new_r.append(i[:j] + s[0] + i[j:])

    return new_r


x = all_perm(s1)
print(len(x))



