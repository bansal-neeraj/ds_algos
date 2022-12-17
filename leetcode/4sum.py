"""
LC - 18
"""
target = 8
# nums = [1, 0, -1, 0, -2, 2]
nums = [2, 2, 2, 2, 2]
nums.sort()
result = []

for i in range(len(nums)-4 + 1):
    if i == 0 or nums[i] != nums[i-1]:
        for j in range(i+1, len(nums)-3 + 1):
            tmp_target = target - (nums[i] + nums[j])
            start = j + 1
            end = len(nums) - 1
            while start < end:
                s = nums[start] + nums[end]
                if s < tmp_target:
                    start += 1
                elif s > tmp_target:
                    end -= 1
                else:
                    result.append([nums[i],nums[j],nums[start],nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[i] == nums[i-1]:
                        start += 1

print(result)


