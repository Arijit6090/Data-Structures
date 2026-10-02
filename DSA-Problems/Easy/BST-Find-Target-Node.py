# Find a Node in a Binary Search Tree
# Accepted
# easy

# Tags

# Companies

# Hints
# You are given the root of a binary search tree (BST) and an integer val. Your task is to find the node in the BST such that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

# When traversing the binary search tree, you should start at the root and decide whether to move to the left subtree or to the right subtree based on whether the value you're searching for is less than or greater than the current node's value. This is possible because in a binary search tree, the left child of a node always has a smaller value, and the right child of a node always has a larger value compared to the node itself.

# Examples:
# Example 1:
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Explanation: We start at root node 4, move to left child 2 which is equal to `val`. Return the subtree rooted at node 2.
# Example 2:
# Input: root = [4,2,7,1,3], val = 5
# Output: []
# Explanation: We start at root node 4, move to right child 7 (since 5 > 4). Node 7 has no left child equal to `val` 5. Hence return null.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findNodeBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        elif root.val == val:
            return root
        elif val < root.val:
            result = self.findNodeBST(root.left, val)
        else:
            result = self.findNodeBST(root.right, val)
        return result