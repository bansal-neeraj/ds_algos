# dynamic programming to calculate fibonacci numbers


def fib1(n):
    if n == 0:
        return 0
    elif n== 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


print(fib1(6))

mem1 = {}
def fib2(n,mem2):
    if n in mem2:
        return mem2[n]

    if n == 0:
        mem2[n] = 0
    elif n == 1:
        mem2[n] = 1
    else:
        mem2[n] = fib2(n-1,mem2) + fib2(n-2,mem2)

    return mem2[n]

print(fib2(6,mem1))






