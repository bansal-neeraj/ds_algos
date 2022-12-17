'''
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers
in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

'''

arr = [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]
arr.sort()
t = len(arr) // 2
new_arr = []

arr1 = arr[:t]
arr2 = arr[t:]
print(arr1)
print(arr2)

s_arr1 = set(arr1)
s_arr2 = set(arr2)

s1_arr_len = len(s_arr1)
s2_arr_len = len(s_arr2)
print(s_arr1)
print(s_arr2)

result = s1_arr_len if s1_arr_len < s2_arr_len else s2_arr_len
print(result)

# method 2
arr = [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]
s_set = set (arr)
s_count = [(i,arr.count(i)) for i in s_set]

s_count.sort(key=lambda c:c[1],reverse=True)
print(s_count)
s = 0
for index,i in enumerate(s_count,start=1):
    s+= i[1]
    if s>=t:
        print(t)
        print(index)
        break

