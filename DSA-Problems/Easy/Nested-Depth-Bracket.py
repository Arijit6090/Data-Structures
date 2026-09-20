# Given a valid parentheses string `s`, return the nesting depth of `s`. The nesting depth is the maximum number of nested parentheses.

# Example 1:

# ```
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation: Digit 8 is inside of 3 nested parentheses in the string.
# ```

# Example 2:

# ```
# Input: s = "(1)+((2))+(((3)))"
# Output: 3
# Explanation: Digit 3 is inside of 3 nested parentheses in the string.
# ```

# Example 3:

# ```
# Input: s = "()(())((()()))"
# Output: 3
# ```

# Your task is to analyze the string and determine the maximum depth of nested parentheses. You'll need to keep track of how many open parentheses you encounter, and at any point, find the maximum number that is open 
class Solution:
    def maxDepth(self, s: str):
        if len(s) == 0:
            return None
        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False
        stack = []
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
                count = len(stack)
            else:
                if s[i] == ")":
                    stack.pop()
        return count