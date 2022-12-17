# split array , using heaps
import heapq


def split_seq(arr):
    v = []
    for i in arr:
        print(v)
        if not v:
            new_item = (i,i-i+1,[i,i])
            heapq.heappush(v,new_item)
        else:
            l_item = heapq.heappop(v)
            last_ele = l_item[2][1]
            if i - last_ele == 1:
                new_item = (i, l_item[1] + 1, [l_item[2][0], i])
                heapq.heappush(v, new_item)
            elif i - last_ele == 0 or i - last_ele > 1:

                if l_item[1] < 3:
                    return False
                else:
                    new_item = (i,1, [i, i])
                    # print(new_item)
                    heapq.heappush(v, new_item)
                    heapq.heappush(v, l_item)

    for j in v:
        print(j)
        if j[1] < 3:
            return False

    return True


if __name__ == '__main__':
    a = [1, 2, 3, 3, 4, 5]
    b = [1,2,3,3,4,4,5,5]
    c = [1,2,3,4,4,5]
    print(split_seq(b))
