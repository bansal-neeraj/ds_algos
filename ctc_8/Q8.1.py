# using recursion and dynamic programming to calculate 

def count_ways(n):
    """ only recursion"""
    if n-3>=0:
        return count_ways(n-3) + count_ways(n-2) + count_ways(n-1)
    elif n-2 >=0:
        return count_ways(n - 2) + count_ways(n - 1)
    elif n-1>=0:
        return count_ways(n-1)
    else:
        return 1


print(count_ways(5))

# def dp_count_ways(n):
#     if n<0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return dp_count_ways(n-3) + dp_count_ways(n-2) + dp_count_ways(n-1)


# print(dp_count_ways(4))
steps_dict = {}
def dp_count_ways(n,steps):
    """recursion and memoization"""
    if n in steps:
        return steps[n]

    if n-3>=0:
        steps[n] = count_ways(n-3) + count_ways(n-2) + count_ways(n-1)
        return steps[n]
    elif n-2 >=0:
        steps[n] = count_ways(n - 2) + count_ways(n - 1)
        return steps[n]
    elif n-1>=0:
        steps[n] = count_ways(n-1)
        return steps[n]
    else:
        return 1


print(dp_count_ways(5,steps_dict))