from collections import namedtuple

person = namedtuple('person','name age marks')

x = person('n1',10,20)
x1 = person('n1',10,40)
x3 = person('n1',30,20)
x4 = person('n1',10,100)


new_list = [x3,x,x1,x4]

print(new_list)

new_list.sort(key=lambda x:(x.age,-x.marks))

print(new_list)