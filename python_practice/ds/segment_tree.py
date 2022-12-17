 # build a segment tree to find the sum of a particular range

def build(sg_tree,n):
    """calculate sum of each pair of leafs , and store the sum, loop run backwards"""
    for i in range(n-1,0,-1):
        # sg_tree[i] = max(sg_tree[2*i] , sg_tree[2*i + 1])
        sg_tree[i] = sg_tree[2*i] + sg_tree[2*i + 1]


def store (sg_tree,arr):
    """store the values of the given array in second half of another array"""
    n = len(arr)
    for i in range(n):
        sg_tree[i + n] = arr[i]


def update(sg_tree,arr,index,val):
    """update a value in array and also the corresponding sums"""
    actual_pos = len(arr) + index
    sg_tree[actual_pos] = val

    while actual_pos >0:
        left = actual_pos
        right = actual_pos
        if actual_pos % 2 == 0:
            right += 1
        else:
            left -= 1

        sg_tree[actual_pos //2] = sg_tree[left] + sg_tree[right]
        actual_pos = actual_pos //2


def find_sum(sg_tree,arr_len,left,right):
    """calculate the sum of the range"""
    left += arr_len
    right += arr_len
    range_sum = 0
    while left <= right:
        if left % 2 == 1:  # means parent of this node contains an element outside the range
            range_sum += sg_tree[left]
            left += 1
        if right % 2 == 0:  # means parent of this node contains an element outside the range
            range_sum += sg_tree[right]
            right -= 1

        left = left // 2
        right = right // 2

    return range_sum


def main():
    arr = [6,10,5,23,12,16]
    sg_tree = [0] * 2 * len(arr)
    store(sg_tree,arr)
    print(f'{sg_tree=}')
    build(sg_tree,len(arr))
    print(f'{sg_tree=}')
    # update(sg_tree,arr,3,4)
    # print(f'{sg_tree=}')
    print(find_sum(sg_tree,len(arr),0,2))


if __name__ == '__main__':
    main()
    print(update.__doc__)


