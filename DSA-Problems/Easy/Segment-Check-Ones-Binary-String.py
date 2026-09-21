# Given a binary string `s` without leading zeros, determine if `s` contains at most one contiguous segment of ones. If the condition is satisfied, return `true`, otherwise return `false`.

# Example 1:

# ```
# Input: s = "1001"
# Output: false
# Explanation: The ones in the string do not form a contiguous segment.
# ```

# Example 2:

# ```
# Input: s = "110"
# Output: true
# Explanation: All the ones in the string are contiguous.
# ```

# In this problem, a binary string is considered valid if there is at most one uninterrupted segment of '1's, with no '0's interrupting this segment. Your task is to verify this condition for any given binary string `s`.

class Solution:
    def isSingleSegment(self, s: str) -> bool:
        if len(s) == 0:
            return False
        if len(s) == 1 and s[0] == '1':
            return True
        if len(s) == 2 and s[0] == '1':
            return True
        for i in range(len(s)-1):
            if s[i] == s[i+1] == '1':
                return True
        return False