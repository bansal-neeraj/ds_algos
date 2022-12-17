import heapq
import random
from queue import PriorityQueue

# a = [(random.randint(1,10),random.randint(1,100)) for x in range(10)]
a = [random.randint(1,100) for x in range(10)]

print(a)

# heapq.heapify(a)

# print(a)
# print(heapq.heappop(a))
# print(a)
# print(heapq.nsmallest(4,a))
# print(a)
print(heapq.nlargest(4,a))
# v = []
# for x in a:
#     heapq.heappush(v,x)
#
# print(v)
#
# # print(heapq.heappop(a))
# # print(heapq.heappop(v))
# # print(v)
# # print(heapq.heappop(v))
# # print(heapq.heappop(v))
#
# q1 = PriorityQueue()
# for x in a:
#     q1.put(x)
#
# while not q1.empty():
#     print(q1.get(),end=',')




