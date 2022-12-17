"""
to modify a variable defined outside a function , define variable with global keyword,
without using global keyword only value can be accessed but not modified.
"""
# def first():
#     def second():
#         nonlocal x
#         x = 10
#
#     x = 5
#     second()
#     print(x)
#
#
# first()

nums = 15


def f1():
    # global nums
    print(nums)
    # nums += 2
    # x = nums + 2
    # print(x)

f1()
print(nums)
