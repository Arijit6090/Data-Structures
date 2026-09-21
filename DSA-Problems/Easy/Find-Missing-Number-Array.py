# Given an array `nums` containing `n` distinct numbers in the range (\[0, n\]), return the only number in the range that is missing from the array.

# #### Example:

# ```
# Input: nums = [3, 0, 1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range 0-3. 2 is the number missing from the array.
# ```

# ```
# Input: nums = [0, 1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range 0-2. 2 is the missing number.
# ```

# ```
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range 0-9. 8 is the missing number.
# ```

# ```
# Input: nums = [0]
# Output: 1
# Explanation: n = 1 since there is 1 number, so all numbers are in the range 0-1. 1 is the missing number.
# ```

class Solution:
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]+1 != nums[i+1]:
                return nums[i] + 1
        return nums[-1]+1