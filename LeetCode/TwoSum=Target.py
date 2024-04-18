def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
nums=[4,5,6,7,8,9]
target=12

result = two_sum(nums,target)
print(result)