# Given an array of integers `arr`, find the sum of `min(b)` for every contiguous subarray `b` of `arr`. Since the result can be quite large, return the final result modulo `10^9 + 7`.

# Example 1:

# ```
# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
# ```

# Example 2:

# ```
# Input: arr = [11,81,94,43,3]
# Output: 444
# ```

# The task is to consider all possible contiguous subarrays of the given array, determine the minimum element of each subarray, and finally sum up all these minimum values, returning this sum modulo `10^9 + 7`. The solution should efficiently handle arrays that can be as long as 30,000 elements with values up to 30,000.
 3 1 2 4
class Solution:
    def sum_of_minimums_in_subarrays(self, arr):
        stack_arr = []
        lv = len(arr)
        frame = 1
        while lv > 0:
            if frame == 1:
                for i in range(len(arr)):
                    stack_arr.append(arr[i])
            else:
                subarr = frame - 1 
                for j in range(len(arr)):
                    smallest = arr[j]
                    for k in range(j, subarr):
                        if arr[k] < smallest:
                            smallest = arr[k]
                    stack_arr.append(smallest)
            lv -= 1
            frame += 1
        sum = 0
        for p in range(len(stack_arr)):
            sum = sum + stack_arr[p]
        return sum

