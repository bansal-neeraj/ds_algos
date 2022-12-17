"""
reverse an integer

LC - 7
"""

n = 45678

def rev_int(x):
    tmp_num = 0
    while x:
        d,r = divmod(x,10)
        tmp_num = tmp_num * 10 + r
        x = d

    return tmp_num


print(rev_int(n))