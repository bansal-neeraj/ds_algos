def buysell(a):
    i = 0
    max_p = 0
    while i < len(a)-1:
        firstbuy = a[i]
        print(firstbuy)
        sell_prices = a[i+1:]
        s1 = find_max(sell_prices)
        print(f'{s1=}')
        if firstbuy > s1:
            i += 1
            continue
        else:
            if s1 - firstbuy > max_p:
                max_p = s1 - firstbuy
            for j in range(i+1,len(a)):
                if a[j] >= firstbuy:
                    continue
                else:
                    i = j
                    break
            else:
                break
    return max_p

def find_max(s):
    max_p = 0
    for i in s:
        if i>max_p:
            max_p = i

    return max_p

l = [7,1,5,3,6,4]
l2 = [7,6,4,3,1]
l3 = [1]
l4 = [2,1,4]
print(buysell(l4))

