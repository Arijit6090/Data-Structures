# Missing Number Hunt

# Given an integer array arr of length n - 1 that contains distinct numbers taken from the range [1, n], exactly one number from this range is absent. The task is to identify and return the missing integer.
# Input: An array arr of size n‑1 with distinct values, each between 1 and n inclusive.
# Output: The single integer from 1 to n that does not appear in arr.

# Example
# Input: arr = [5, 1, 3, 4]
# Output: 2
# Explanation: The numbers should be 1 through 5. The array lacks the value 2, so the answer is 2.
class Solution:
    def findMissingNumber(self, arr):
        if len(arr) == 0:
            return 1

        sortarr = sorted(arr)

        if sortarr[0] != 1:
            return 1

        if len(sortarr) == 1:
            return 2

        else:
            for i in range(len(sortarr) - 1):
                if ((sortarr[i] + 1) != sortarr[i+1]):
                    return (sortarr[i] + 1)
        return (sortarr[i+1] + 1)

obj = Solution()

print(obj.findMissingNumber([]))