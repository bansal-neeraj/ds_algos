"""
free variable - variable used in a code block but not defined there
locals() -  Return a dictionary containing the current scope's local variables.

if the value of an immutable free variable is changed , python creates a separate local variable with a different id,
but mutable variable is NOT created new
"""


def f1():

    x = 'abc'
    def f2():
        x = 15
        print(x)
        print(id(x))
        y = 10
        print(locals())

    f2()
    print(f'x in outside function {x=}')
    print(id(x))

f1()

# help(locals)

print('-'*50)
def f3():
    nums = [2]

    def f4():
        nums.append(3)
        print(nums)

    f4()
    print(nums)
f3()