# find sqrt without using ** operator

def find_sqrt(x):
    start = 0
    end = x
    while start <= end:
        mid = (start + end) //2
        tmp_prod = mid * mid
        if tmp_prod == x:
            return mid
        elif tmp_prod < x:
            start = mid +1
        else:
            end = mid -1

    return mid -1 if mid * mid > x else mid


x = 23
print(find_sqrt(x))