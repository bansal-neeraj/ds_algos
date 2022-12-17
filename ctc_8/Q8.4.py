# multiply two number without using 8 operator

def first_function(n1,n2):
    smaller = n1 if n1 < n2 else n2
    bigger = n1 if n1 >= n2 else n2
    print(recursive_multiply(smaller,bigger))


def recursive_multiply(smaller,bigger):
    if smaller == 1:
        return bigger
    if smaller == 0:
        return 0

    if smaller % 2 == 0:
        return 2 * recursive_multiply(smaller // 2,bigger)

    else:
        return 2 * recursive_multiply(smaller // 2, bigger) + bigger


first_function(30,5)
