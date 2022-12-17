import heapq

a = [2,4,1,0,7,34]

for i in range(len(a)):
    a[i] = -a[i],i

print(a)

heapq.heapify(a)

# while a:
#     print(heapq.heappop(a))


s = heapq.nlargest(3,a)
print(s)




