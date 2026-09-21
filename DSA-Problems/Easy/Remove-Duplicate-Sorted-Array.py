# Remove Duplicates from Sorted Collection
# easy

# Tags

# Companies

# Hints
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Imagine you have a collection of numbered cards arranged neatly in a line. Each number represents a unique value, and all the cards with the same number are grouped together because they are sorted. Your task is to find a way to keep only one card of each number and remove the rest, while maintaining the order of numbers. In the end, count how many different numbers you retained in your collection.

# Your objective is to modify the array directly to achieve this without creating a new array. At the end of the process, return the number of unique numbers left in the array.

# Example 1

# Input: nums = [1, 1, 2]
# Output: 2
# Explanation: Keep 1, remove the duplicate 1, keep 2. The final array state for the first k elements is [1, 2]. 
# Example 2

# Input: nums = [0, 0, 1, 1, 1, 2, 2]
# Output: 3
# Explanation: Keep 0, 1, and 2 once each and remove all extra duplicates. The final array state for the first k elements is [0, 1, 2]. 

class Solution:
    def removeDuplicates(self, nums):
        count = []
        count.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] != count[-1]:
                count.append(nums[i])
        return len(count)