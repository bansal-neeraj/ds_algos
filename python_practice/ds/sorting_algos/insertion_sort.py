a = [3,1,5,0,-2,10,11]

for i in range(1,len(a)):
    if a[i] < a[i-1]:
        j = i
        anchor = a[i]
        while j>= 1 and a[j] >= anchor:
                a[j] = a[j-1]
                j -=1
        a[j] = anchor

print(a)