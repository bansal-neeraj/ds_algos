"""
kane's algorithm -
to solve - maximum subarray problem

find local maximum at each index by comparing the element at that index and sum all elements till
that index includig the element,

local maximum
global maximum

compare every local maxmum to a global maximum and replace global maximum if local maximum is greater
"""

def kane(arr):
    s = arr[0]
    max_global = s
    for i in range(1, len(arr)):
        s += arr[i]
        s = max(s, arr[i])
        if s > max_global:
            max_global = s

    return max_global


def main():
    a = [10,2,-5, 4, 6, -3, 4, -1]
    print(kane(a))


if __name__ == '__main__':
    main()