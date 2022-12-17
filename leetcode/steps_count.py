import time


def count_steps(n):
    if n == 0:
        return 1
    if n-2 >= 0:
        return count_steps(n-2) + count_steps(n-1)
    elif n-1 >= 0:
        return count_steps(n-1)


my_dict = {}


def count_steps_dp(n):
    if n == 0:
        return 1
    if n-2 >= 0:
        if (n-2) not in my_dict:
            my_dict[n-2] = count_steps_dp(n-2)
        if (n-1) not in my_dict:
            my_dict[n-1] = count_steps_dp(n-1)
        return my_dict[n-2] + my_dict[n-1]
    elif n-1 >= 0:
        if (n-1) not in my_dict:
            my_dict[n-1] = count_steps_dp(n-1)
        return my_dict[n-1]


n = 15
start1= time.perf_counter()
print(count_steps(n))
end1 = time.perf_counter()

print(end1-start1)

start= time.perf_counter()
print('withy dp...',count_steps_dp(n))
end = time.perf_counter()

print(end-start)