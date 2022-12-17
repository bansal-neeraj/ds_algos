n = 789
print(bin(n))
c = 0
while n:
    n = n & (n-1)
    print(bin(n))
    c +=1

print(c)