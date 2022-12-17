# create an iterator, list command / function is calling the iterator
# range function as way to crete a list
from collections import namedtuple

class MyIter:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        val = self.num
        self.num = val + 1
        if val > 10:
            raise StopIteration
        else:
            return val

myiter_obj = MyIter()

# print(next(myiter_obj))
# print(next(myiter_obj))
# print(list(myiter_obj))

# using range function to generate a list , as per stackoverlfow range is an iterator , but next is not working

# print ("**"*10 )


x = range(20)
print(x)

short_date = list(x)

# print(short_date)

if 4 in x:
    print('found')
else:
    print('not found')


