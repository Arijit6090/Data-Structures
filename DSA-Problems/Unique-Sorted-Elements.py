# Given a **sorted** array `arr[]` of length `n`, modify the array **in‑place** so that all distinct values appear at the beginning of the array while preserving their original order. After the distinct segment, the remaining positions may contain any values and are irrelevant for the result.

# The function should return the length of the prefix that contains the unique elements.

class Solution:
    def uniqueSortedElements(self, arr):
        distinct = []

        for i in range(len(arr)):
            if len(distinct) == 0:
                distinct.append(arr[i])
            elif (distinct[-1] != arr[i]):
                distinct.append(arr[i])
        return len(distinct)
#         print(len(distinct))
#         print(distinct)

# obj = Solution()

# obj.uniqueSortedElements([1,2,3,3,4,5,6])