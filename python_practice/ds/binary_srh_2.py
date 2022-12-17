"""
binary search - find the lowest index - 28Nov JIO interview
"""

import random

arr = [0,1,1, 2, 2, 2, 2, 4, 4, 5, 6]
v = 0


def bin_srh(value,a,start,end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if a[mid] == value:
        if mid == 0 or a[mid-1] != a[mid]:
            return mid
        else:
            return bin_srh(value,a,start,mid-1)
    if a[mid] < value:
        return bin_srh(value,a,mid+1,end)
    else:
        return bin_srh(value,a,start,mid-1)


print(
    bin_srh(v,arr,0, len(arr)-1)
)
