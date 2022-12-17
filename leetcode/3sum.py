"""
LC 15 - 3S
"""

nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 1, 1]
# nums = [0,0,0]


final_list = []
s = set()
for i in range(len(nums)):
    if nums[i] in s:
        continue

    s.add(nums[i])

    target = (nums[i] - 0) * -1
    my_dict = {}

    for j in range(i+1,len(nums)):
        ele = target - nums[j]
        if ele in my_dict:
            final_list.append([ele,nums[j],nums[i]])
            # t = [ele,nums[j],nums[i]]
            # t.sort()
            # if t not in final_list:
            #     final_list.append(t)
        else:
            my_dict[nums[j]] = True


print(final_list)




