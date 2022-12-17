"""
XOR operator - if both bits are same it will give 0, if either bit is 1 and other is 0 , output is 1

1 ^ 1 = 0
0 ^ 0 = 0
1 ^ 0 = 1
0 ^ 1 = 1

1. when a number is xor with itself , result is always 0
2. when a number is xor with 0 , result is number itself

"""
#  find the missing number - LeetCode - Q268

a = [0,1,3]

z = len(a)

for index, i in enumerate(a):
    z = z ^ index ^ i

print(z)
