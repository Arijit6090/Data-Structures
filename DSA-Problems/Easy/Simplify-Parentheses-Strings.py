class Solution:
    def simplifyParentheses(self, s: str):
        stack = []
        depth = 0
        for i in s:
            if i == "(":
                if depth > 0:
                    stack.append(i)
                depth += 1
            else: # i == ")"
                depth -= 1
                if depth > 0:
                    stack.append(i)
        return "".join(stack)
            