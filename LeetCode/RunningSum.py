def running_sum(nums):
    # Initialize the running sum to zero
    running_sum = 0
    # Iterate over the list and calculate the running sum at each index
    for i in range(len(nums)):
        running_sum += nums[i]
        print(running_sum)
        nums[i] = running_sum
    return nums
nums=[1,2,6,4]
print(running_sum(nums))