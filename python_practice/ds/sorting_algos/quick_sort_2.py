"""
quick sort , uses recirsive function and a partition function
"""

# a = [0, -2, 10, 3, 45, 0, -1, -2]
a = [-6, -3, 4, -2, 10, 11]

def qs(arr, start, end):
    if start >= end:
        return None

    new_index = partition(arr, start, end)
    qs(arr, start, new_index-1)
    qs(arr, new_index + 1, end)


def partition(arr, l, r):

    pivot = arr[r]
    i = l-1
    for j in range(l, r):

        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


qs(a, 0, len(a) - 1)
print(a)

