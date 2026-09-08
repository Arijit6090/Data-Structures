# Is List in Ascending Order
# Given an integer array `arr`, determine whether the elements are arranged in non‑decreasing order (each element is **less than or equal to** the next one). Equal values are allowed, and any pair of consecutive equal values is considered sorted. Return `true` if the entire array satisfies this condition; otherwise, return `false`.
class Solution:
    def isAscending(self, arr):
        for i in range(len(arr) - 1):
            if (arr[i+1] < arr[i]):
                return False
        return True

obj = Solution()

print(obj.isAscending([8, 8, 9, 8]))