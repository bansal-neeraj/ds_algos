from collections import Counter

start = "AACCGGTT"
end = "AACCGGTA"

c1 = Counter(start)
c2 = Counter(end)

c2.subtract(c1)

print(c2)