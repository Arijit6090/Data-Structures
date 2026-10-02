# Postorder Traversal of Binary Tree
# easy

# Tags

# Companies

# Hints
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:
# Input:

# root = [10,null,15,5]
# Output:

# [5,15,10]
# Example 2:
# Input:

# root = [4,7,3,1,2,null,9,null,null,6,8,11]
# Output:

# [1,6,8,2,7,11,9,3,4]
# Example 3:
# Input:

# root = []
# Output:

# []
# Example 4:
# Input:

# root = [20]
# Output:

# [20]
# Example 5:
# Input:

# root = [5,3,8,null,null,6,9,null,7]
# Output:

# [3,7,6,9,8,5]
# Note:
# Perform a postorder traversal by visiting the left child, then the right child, and finally the parent node. This traversal is usually used to delete the tree as all children are visited before the parent. The challenge is to perform this task iteratively, without using recursion. The tree's nodes can range from 0 to 100, and node values can be between -100 to 100.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        result = []
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            traverse(node.right)
            result.append(node.val)

        traverse(root)
        return result
        
