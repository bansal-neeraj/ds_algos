"""
expressions in default arguments are calculated when function is defined , and not when it is called
"""


def f1(val,list=[]):
    print(id(list))
    list.append(val)
    return list


list1 = f1(10)
list2 = f1(20,[])
list3 = f1('a')

print(list1)
print(list2)
print(list3)

# # ################### Q2 - closures

def multipliers():
    return [lambda x: i * x for i in range(4)]


print ([m(2) for m in multipliers()])