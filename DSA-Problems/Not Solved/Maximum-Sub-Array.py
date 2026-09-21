# # Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# ### Example 1:

# ```
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# ```

# ### Example 2:

# ```
# Input: nums = [1]
# Output: 1
# Explanation: The array contains only one element, which is the max subarray.
# ```

# ### Example 3:

# ```
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The entire array is the largest subarray with sum = 23.
# ```

class Solution:
    def findMaxSubarraySum(self, nums):
        first_idx = 0
        last_idx = 0
        big_guy = nums[0]
        
        for i in range(len(nums)):
            if nums[i] > big_guy:
                big_guy = nums[i]
                first_idx = i

        sumof = nums[first_idx]
        for j in range(first_idx, len(nums)):
            