n = 4567

print(bin(n))

print(f'binary of 1 is {bin(1)}')

bit = (n >> 0) & 1
print(bin(n))
print(bit)

n = n >> 1
print(bin(n))
