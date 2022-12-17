# Practice on 14Aug

def create_segment(original_arr):
    arr_len = len(original_arr)
    segment_arr = [0] * 2 * arr_len

    for i in range(arr_len):
        segment_arr[arr_len + i] = original_arr[i]

    for j in range(arr_len - 1, 0, -1):
        segment_arr[j] = segment_arr[2 * j] + segment_arr[2 * j + 1]
        # segment_arr[j] = max(segment_arr[2 * j] , segment_arr[2 * j + 1])

    return segment_arr


def update_sum(s_arr, location, value, original_arr):
    loc_in_seg = len(original_arr) + location
    s_arr[loc_in_seg] = value

    if loc_in_seg % 2 == 0:
        parent_loc = loc_in_seg // 2
    else:
        parent_loc = (loc_in_seg - 1) // 2

    while parent_loc > 0:
        s_arr[parent_loc] = max(s_arr[2 * parent_loc] , s_arr[2 * parent_loc + 1])
        # s_arr[parent_loc] = s_arr[2 * parent_loc] + s_arr[2 * parent_loc + 1]
        if parent_loc % 2 == 0:
            parent_loc = parent_loc // 2
        else:
            parent_loc = (parent_loc - 1) // 2


def find_sum(s_arr,start,end,arr_len):
    n_start = arr_len + start
    n_end = arr_len + end
    v = 0

    while n_start <= n_end:
        if n_start % 2 != 0:
            v += s_arr[n_start]
            n_start = (n_start +1) // 2
        else:
            n_start = n_start //2

        if n_end % 2 == 0:
            v += s_arr[n_end]
            n_end = (n_end -1) // 2
        else:
            n_end = n_end //2

    print(f'range sum is {v}')


def main():
    a = [4, 6, 9, 10, 1, 45]  # even count
    b = [4, 6, 9, 10, 1]  # odd count
    c = [6,10,5,2,7,1,0,9]
    d = [7,9,5]
    test_case = c
    seg_arr = create_segment(test_case)
    print(f'{seg_arr=}')
    # update_sum(seg_arr, 4, 3, b)
    # print(f'{seg_arr=}')
    find_sum(seg_arr,0,7,len(test_case))


if __name__ == '__main__':
    main()
