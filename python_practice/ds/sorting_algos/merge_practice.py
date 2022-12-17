a = [3,1,5,0,-2,10,11]


def split(a):
    a_len = len(a)
    if a_len > 1:
        mid_point = a_len // 2
    else:
        return a

    left = split(a[:mid_point])
    right = split(a[mid_point:])

    return combine(left,right)


def combine(left,right):

    tmp_lst = []
    i,j = 0,0

    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            tmp_lst.append(left[i])
            i += 1
        else:
            tmp_lst.append(right[j])
            j += 1

    if i< len(left):
        tmp_lst += left[i:]
    else:
        tmp_lst += right[j:]

    return tmp_lst


print(split(a))

