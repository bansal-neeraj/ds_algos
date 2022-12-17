# Magic index

# test_list = [-2,-1,0,3,7]
# test_list = [1,1,1,1,1]


def magic_index(arr):
    """when all the integers are distinct and sorted in ascending"""
    start = 0
    end = len(arr) -1
    while start <= end:
        mid = (start + end) //2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            start = mid +1
        else:
            end = mid -1

    return -1


# print(magic_index(test_list))

test_list = [-10,-5,1,2,2,3,4,7,9,12,13]


def non_distinct(arr,start,end,arr_len):
    """when integers are not distinct"""
    if start > end:
        return False

    mid = (start + end) //2
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        new_end = arr[mid]
        if 0 <= new_end <= arr_len:
            return non_distinct(arr,start,new_end,arr_len) or non_distinct(arr,mid + 1,end,arr_len)
        else:
            return non_distinct(arr,mid + 1,end,arr_len)
    else:
        new_start = arr[mid]
        if 0 <= new_start <= arr_len:
            return non_distinct(arr, new_start, end, arr_len) or non_distinct(arr,start,mid -1,arr_len)
        else:
            return non_distinct(arr,start,mid -1,arr_len)


print(non_distinct(test_list,0,len(test_list)-1,len(test_list)-1))