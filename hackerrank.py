x = [1, 2, 3, 4, 5]
# x = [1, 2, 3, 5, 9]
# x = [7,2,4,6,5,9,12,11]
x = [5,10]

house = []
x.sort()
for i in range(len(x)-1):
    if x[i+1]-x[i] > 0:
        house += [x[i]] + [0] * (x[i+1]-x[i] -1)
    else:
        house.append(x[i])

house.append(x[-1])

def add_radio(arr,k,c):

    if len(arr) == 0:
        return c
    if len(arr) < k +1:
        return c+1 if any(arr) else c

    if arr[k]:
        c += 1
        return add_radio(arr[k+k+1:], k, c)
    else:
        sub_arr = arr[:k]
        for j in range(len(sub_arr)-1,-1,-1):
            if sub_arr[j]:
                c += 1
                break
        return add_radio(arr[j+k+1:],k,c)


k = 5
print(add_radio(house,k,0))


