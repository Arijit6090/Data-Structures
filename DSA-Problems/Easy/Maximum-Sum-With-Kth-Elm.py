# You are given a **0-indexed** integer array `nums` and an integer `k`. Your task is to perform the following operation **exactly** `k` times in order to maximize your score:

# 1. Select an element `m` from `nums`.
# 2. Remove the selected element `m` from the array.
# 3. Add a new element with a value of `m + 1` to the array.
# 4. Increase your score by `m`.

# Return *the maximum score you can achieve after performing the operation exactly* `k` *times.*

# **Example 1:**

# ```
# Input: nums = [1,2,3,4,5], k = 3
# Output: 18
# ```

class Solution(object):
    def maximizeSum(self, nums, k):
        maxnum = nums[0]
        maxlist = []
        maxsum = 0
        for i in range(1, len(nums)):
            if nums[i] >= maxnum:
                maxnum = nums[i]
        while k>0:
            maxlist.append(maxnum)
            k -= 1
        for i in range(len(maxlist)):
            maxlist[i] = maxlist[i] + i
        for i in range(len(maxlist)):
            maxsum += maxlist[i]
        return maxsum

# better approach:
class Solution(object):
    def maximizeSum(self, nums, k):
        # Find the maximum element in the list
        maxnum = max(nums)
        
        # Apply the arithmetic progression sum formula
        return (maxnum * k) + (k * (k - 1)) // 2
