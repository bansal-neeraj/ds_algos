import itertools

# a = [1,5,1,7,5,7,7]
# a.sort()

a = '00110011'
x = [len(list(v)) for k,v in itertools.groupby(a)]

print(x)
print(x[1:])
z = zip(x,x[1:])

s = sum([min(i) for i in z])
print(s)





