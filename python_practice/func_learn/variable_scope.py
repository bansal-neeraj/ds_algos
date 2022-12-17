"""
to access a variable, defined in the outer function, inside a nested function nonlocal keyword is used
"""
def f1():
    x = 10

    def f2():
        nonlocal x
        x = 30
        print(x)
    f2()
    print(x)

f1()

# ##########################Global Keyword ###########################################
""""
global keyword used when a variable is defined outside a function and same variable needs to be access inside a function
define variable using a global key work
"""
print('-'*50)
foo = 1   # defined outside all functions

def test1():
    print (foo)

def test2():
    global foo
    foo = 4  # this statement will change global variable , if glbal noy
    print(foo)

test1()
test2()

print(foo)


