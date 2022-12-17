# Q1
# check difference between = and += ,
# = creates a new variable
# += does NOT crete a new variable but modiifies existing var but only incase of a mutable object like a list for
# for a non-mutable object like int , Python will create a new variable even for +=

# Q2
# in python, variable defined inside a loop is valid outside of the loop also. Python variable scope is only limited to
# functions

# Q3
# for...else
# else is executed when the loop ends or when it not executed at all, mainly used to identify if the loop was terminated
# because of a break statement or it got completed, or it can be said that else will be called always except when the
# break command terminated the loop,


a = [1,2,3,4]
print('id of a',id(a))
b = a
a = a + [5,6,7]
# a += [5,6,7]
print('id of b',id(b))
print('id of a',id(a))
print(a)
print(b)


c = [1,2,3,4]

d = c
c += [5,6,7]

z = 7901
n1 = z
# print(id(z))
z += 1
# print(id(z))
# print(z)
# print(n1)
print('dictionary question')

x = {
    15:'a'
}

print(x)
for i in x:
    print(i)
    y = 10
    print(id(y))
    # x[2] = 'def'
    print(y)



# --------------------for else ----------------------------------------------------------------
print('checking for....else')
fr_list = [1,2,3,4]

empty_list = []
for i in fr_list:
# for i in empty_list:
    print(i)
    if i == 3:
        break
else:
    print('for else ')