x = 34567

x_copy = x

reverse_x = 0

while x_copy:
    reverse_x = (reverse_x * 10) + x_copy  % 10
    x_copy = x_copy // 10

print(reverse_x)