# MY SOLUTION

# class Solution:
#     def shiftZerosToEnd(self, arr):
#         zeros = []
#         non_zeros = []
#         for i in range(len(arr)):
#             if (arr[i] == 0):
#                 zeros.append(arr[i])
#             else:
#                 non_zeros.append(arr[i])
#         non_zeros.extend(zeros)
#         return non_zeros

# obj = Solution()

# print(obj.shiftZerosToEnd([1,2,0,4,0,3,0,7,0,8,9,7]))

# ACTUAL DSA TYPE APPROACH

class Solution:
    def shiftZerosToEnd(self, arr):

        non_zero = 0

        for i in range(len(arr)):
            if arr[i] != 0:
                # using python way
                # arr[non_zero], arr[i] = arr[i], arr[non_zero]  this means: Put the value at arr[i] into arr[non_zero], and put the old value at arr[non_zero] into arr[i].
                # using a temporary variable:
                temp = arr[non_zero]
                arr[non_zero] = arr[i]
                arr[i] = temp

                non_zero += 1

        return arr


obj = Solution()

print(obj.shiftZerosToEnd([1, 2, 0, 4, 0, 3, 0, 7, 0, 8, 9, 7]))