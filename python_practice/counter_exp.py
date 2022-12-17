from collections import Counter

s = 'abcaacbdadd'
c = Counter(s)

print(c.keys())
print(c.values())
print(c.items())
print(c['def'])
print(c.most_common(2))

