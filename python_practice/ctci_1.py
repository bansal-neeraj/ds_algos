# question 1.9 - string rotation

def check_rotation(s1: str,s2: str) -> bool:
    char_count_dict = dict()
    for i in s1:
        c_char = s1.count(i)
        char_count_dict[i] = c_char

    for j in s2:
        if j in char_count_dict:
            c_char2 = s2.count(j)
            if char_count_dict[j] !=c_char2:
                return False
        else:

            return False

    new_pos = len(s1) - s2.find(s1[0])
    s2_rev = s2[::-1]
    for az in range(len(s2)):
        if s2_rev[az] == s1[0]:
            newpos = az + 1
            break

    print(new_pos)
    print(newpos)

    new_pos_dict = []
    for i in range(len(s1)):
        new_pos_dict.append((s1[i], i - new_pos))

    # create new string with new positions
    new_str = ["" for x in range(len(s1))]
    for z in new_pos_dict:
        new_str[z[1]] = z[0]

    new_str1 = "".join(new_str)
    print(s1)
    print(new_str1)

    # for j in range(len(s2)):
    #     if new_pos_dict[s2[j]] == j:
    #         pass
    #     else:
    #         return False

    return True


s1 = 'waterbottle'
s2 = 'erbottlewat'

print(check_rotation(s1,s2))



