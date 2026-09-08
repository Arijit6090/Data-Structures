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