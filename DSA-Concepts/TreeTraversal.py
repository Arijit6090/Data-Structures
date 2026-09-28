class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def preorder(root):
    if (root != None):
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if (root != None):
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def postorder(root):
    if (root != None):
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)

preorder(root)
print("\n") # 1 3 2 4 5 8 

inorder(root)
print("\n") # 2 3 4 1 5 8 

postorder(root)
print("\n") # 2 4 3 8 5 1 
