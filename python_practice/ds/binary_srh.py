# binary search - return the index of the element else return -1
from random import randint


def find_index_loop(arr,value):
    """binary search , return index . without recursion"""

    start = 0
    end = len(arr) -1

    while start <= end:
        mid = (end + start) // 2
        if arr[mid] == value:
            return mid
        elif value > arr[mid]:
            start = mid + 1
        else:
            end = mid -1

    return -1


def find_index_recursion(arr,value,start=0,end=0):
    # print(f'{start=}')
    # print(f'{end=}')
    if start <= end:
        mid = (start + end) //2
        if arr[mid] == value:
            return mid
        elif value > arr[mid]:
            return find_index_recursion(arr,value,mid + 1,end)
        else:
            return find_index_recursion(arr, value, start, mid -1)
    else:
        return -1


def binary_find(arr,value):
    """binary search using recursion"""
    in_len = len(arr)
    if in_len:
        mid = len(arr) // 2
        if arr[mid] == value:
            return True
        elif value>arr[mid]:
            return binary_find(arr[mid+1:],value)
        else:
            return binary_find(arr[:mid], value)
    else:
        return False


def binary_find_loop(arr,value):
    """binary search without recursion"""
    tmp_arr = arr
    in_len = len(tmp_arr)

    while in_len !=0:
        mid = in_len // 2
        if tmp_arr[mid] == value:
            return True
        elif value > tmp_arr[mid]:
            tmp_arr = tmp_arr[mid+1:]
        else:
            tmp_arr = tmp_arr[:mid]

        in_len = len(tmp_arr)

    return False


def insert_index(arr,value,start,end):
    """find the index where element is present or return index where it should be inserted"""
    if start == end:
        if arr[start] == value:
            return start
        else:
            return start if value < arr[start] else start +1

    mid = (start + end) // 2
    if arr[mid] == value:
        return mid
    elif value < arr[mid]:
        return insert_index(arr,value,start,end-1)
    else:
        return insert_index(arr, value, mid+1, end)



test_list = list(map(lambda y:randint(1,100),range(10)))
test_list.sort(reverse=False)
# test_val1 = test_list[randint(0,9)] to randomly pick a number present in the list
test_val1 = randint(0,99)  # to randomly pick a number that may or may NOT be preset in the list


print(f'{test_val1=}')
print (binary_find(test_list, test_val1))
print (binary_find_loop(test_list, test_val1))
# print (binary_find(test_list, 51))
# print (binary_find_loop(test_list, 51))

# print(f'{test_list.index(test_val1)=}')
print('index via loop',find_index_loop(test_list,test_val1))
print('index via recursion',find_index_recursion(test_list,test_val1,0,len(test_list)))
print(test_list)

test_list = [1,3]
test_val1 = 0
print('find insert index ',insert_index(test_list,test_val1,0,len(test_list)-1))


# print (binary_search(test_list, test_val2))
