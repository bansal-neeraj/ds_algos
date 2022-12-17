# Quick sort, TO BE CHECKED , LOGIN WORKING BUT NOT AS PER STANDARD PROCESS

def split(a):
    a_len = len(a)
    if a_len <= 1:
        return a
    else:
        pivot = a[-1]
        low_lst , high_lst = [],[]
        for i in a:
            if i < pivot:
                low_lst.append(i)
            elif i > pivot:
                high_lst.append(i)

        # print(low_lst,pivot,high_lst)
        return split(low_lst) + [pivot] + split(high_lst)



print(split(a))



