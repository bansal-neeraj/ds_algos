"""
Depth first search travlersal for a 2d matrix
method - check all four directins in a set sequence i.e. top,right,bottom,left
"""


def dfs(r, c, rows, cols, my_dict, arr_val, arr):
    if (r, c) in my_dict:
        return
    my_dict[(r, c)] = True
    # arr_val.append(arr[r][c])
    if arr[r][c] == 1:
        arr_val.append((r,c))

    if r - 1 >= 0:  # top
        dfs(r - 1, c, rows, cols, my_dict, arr_val, arr)
    if c + 1 <= cols:  # right
        dfs(r, c + 1, rows, cols, my_dict, arr_val, arr)
    if r + 1 <= rows:  # down
        dfs(r + 1, c, rows, cols, my_dict, arr_val, arr)
    if c - 1 >= 0:  # left
        dfs(r, c - 1, rows, cols, my_dict, arr_val, arr)

    return arr_val


def main():
    arr = [
        [10, 23, 56, 89],
        [78, 90, 27,124],
        [77, 43, 9, 12]
    ]

    # arr = [
    #     [1, 2, 3, 4, 5],
    #     [6, 7, 8, 9, 10],
    #     [11, 12, 13, 14, 15],
    #     [16, 17, 18, 19, 20]
    # ]

    arr = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]

    rows = len(arr) - 1
    cols = len(arr[0]) - 1
    l = dfs(0,0,rows,cols,{},[],arr)
    print(l)


if __name__ == '__main__':
    main()
