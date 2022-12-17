"""
LC - 40
"""
from collections import Counter

candidates = [10,1,2,7,6,1,5]
target = 8
c = Counter(candidates)
counter_list = c.most_common()
print(counter_list)
result = []


def combination_sum(new_list,curr,counter,t):
    print(new_list)
    if t == 0:
        result.append([*new_list])
    elif t < 0:
        return
    else:
        for i in range(curr,len(counter)):
            cand, fq = counter[i]
            if fq <=0:
                continue
            new_list.append(cand)
            counter[i] = (cand,fq-1)
            combination_sum(new_list,i,counter,t-cand)
            new_list.pop()
            counter[i] = (cand, fq)


combination_sum([],0,counter_list,target)
print(result)


