# find all permutations of a string of unique characters
def add_char(s1,c):
    new_str_list = []
    for i in range(len(s1)+1):
        new_str_list.append(s1[:i] + c + s1[i:])

    return new_str_list


def compute_per(s):
    if len(s) > 2:
        # print(s[-1],s[:-1])
        p = compute_per(s[:-1])
        tmp_list = []
        for j in p:
            tmp_list += add_char(j,s[-1])
        return tmp_list

    else:
        # print(s)
        return [
            s[0] + s[1],
            s[1] + s[0]
        ]


s = 'abcdef'
result = compute_per(s)
print(len(result))


# add_char('abc','d')
