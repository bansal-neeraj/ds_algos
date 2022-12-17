
def merge_sort(a_new):

    a_len = len(a_new)
    if a_len <2:
        return a_new
    else:
        mid = a_len //2

        return merge_combine(merge_sort(a_new[:mid]),merge_sort(a_new[mid:]))


def merge_combine(c,d):
    i,j =0,0
    tmp_arr = []
    while i<len(c) and j < len(d):
        if c[i] < d[j]:
            tmp_arr.append(c[i])
            i = i+1
        else:
            tmp_arr.append(d[j])
            j = j+1

    if i == len(c):
        return tmp_arr + d[j:]
    else:
        return tmp_arr + c[i:]


a = [9,2,4,3,6,7,1]

print(merge_sort(a))

