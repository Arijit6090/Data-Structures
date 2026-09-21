class Solution:
    def findErrorNums(self, nums):
        nums.sort()
        answer = []

        if len(nums) == 2 and nums[0] == nums[1]:
            answer.append(nums[0])
            answer.append(nums[0]+1)
            return answer

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                if len(answer) == 0 or answer[-1] != nums[i]:
                    answer.append(nums[i])
            elif nums[i]+1 != nums[i+1]:
                answer.append(nums[i]+1)

        if nums[0] != 1:
            answer.append(nums[0]-1)

        return answer