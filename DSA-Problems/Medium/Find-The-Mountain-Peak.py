class Solution:
    def findPeakIndex(self, arr):
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right)//2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else: 
                right = mid
        return right # can be also return left, the loop stops only when left == right
        
                