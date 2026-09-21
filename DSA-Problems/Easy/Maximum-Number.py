# You are given a positive integer `num` consisting only of digits `6` and `9`.

# Return *the maximum number you can get by changing **at most** one digit (*`6` *becomes* `9`*, and* `9` *becomes* `6`*)*.

# **Example 1:**

# ```
# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
# ```

class Solution(object):
    def maximizeNumber(self, nums):
        initial = nums
        numbers = []
        while nums>0:
            numbers.append(nums%10)
            nums = nums//10
        revnums = list(reversed(numbers))
        if revnums[0] == 6:
            revnums[0] = 9
            return int("".join(map(str,revnums)))
        for i in range(1, len(revnums)):
            if revnums[i] == 6:
                revnums[i] = 9
                return int("".join(map(str,revnums)))
        return initial