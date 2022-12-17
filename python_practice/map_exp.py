a = [1, 2, 4, 6]

def f1(x):
    return 2 * x

y = map(f1,a)

print(next(y))
print(next(y))