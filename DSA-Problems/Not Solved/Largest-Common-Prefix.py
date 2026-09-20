# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string `""`.

# Example 1:

# ```
# Input: strs = ["windtalker","windy","wind"]
# Output: "wind"
# ```

# Example 2:

# ```
# Input: strs = ["cat","dog","elephant"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# ```

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                