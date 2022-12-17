"""
why set is printing in sequential because integers hash to themselves and when a set is resized internally , all the
integers are stored in their respective hashes
"""
import random
from sys import getsizeof

s = set()
while len(s)< 50:
    x = random.randint(1,50)
    s.add(x)
    if len(s) % 5 == 0:
        print(id(s),getsizeof(s),s)


print(random.sample(range(50),50))


