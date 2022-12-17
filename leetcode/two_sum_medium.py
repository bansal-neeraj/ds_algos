"""
lc -167
"""

arr = [2,7,11,15]
target = 9

i, j = 0, len(arr) -1
while i < j:
    s = arr[i] + arr[j]
    if s == target:
        print([i+1,j+1])
        break
    elif s > target:
        j -= 1
    else:
        i += 1

