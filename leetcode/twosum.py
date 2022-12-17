'''
x = [10,20,30,40,20,80]

y = [*range(len(x))]

z = list(zip(x,y))

print(f'{y=}')
print(f'{z=}')
n_dict = {}

for i in z:
    if i[0] in n_dict:
        n_dict[i[0]] = [n_dict[i[0]],i[1]]
    else:
        n_dict[i[0]] = i[1]


print(n_dict)
'''
# ################################practice 3
print('-'*25)

# nums = [2,1,5,3]
# t = 4
nums = [2,7,11,15]
t = 9

# nums = [3,3]
# t = 6
my_dict = {}
for index,i in enumerate(nums):
    d = t - i
    if d not in my_dict:
        my_dict[i] = index
    else:
        print(index,my_dict[d])





