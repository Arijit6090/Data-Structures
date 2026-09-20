# Reverse the given array `arr[]`. Reversing an array means rearranging its elements so that the first element becomes the last, the second element becomes the second‑last, and so on.
# ```
# Input: arr[] = [1, 4, 3, 2, 6, 5]
# Output: [5, 6, 2, 3, 4, 1]
# Explanation: The element `1` moves to the last position, `4` moves to the second‑last, etc.
# ```
class Solution:
    def flipArray(self, arr):
        flip = []
        for i in range(len(arr)):
            flip.append(arr.pop())
        return flip

obj = Solution()

print(obj.flipArray([1,3,2,4,6]))
