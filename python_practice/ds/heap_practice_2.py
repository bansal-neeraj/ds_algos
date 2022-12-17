import heapq
import random
a = [random.randint(-10,100) for i in range(10)]

heapq.heapify(a)

while a:
    print(heapq.heappop(a))



