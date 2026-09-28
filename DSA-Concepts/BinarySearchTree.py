class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def insert(root, value):
    if root == None:
        return Node(value)
    if root.data == value:
        return root
    if value < root.data: 
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root == None:
        print("Element Not Found", end="\n")
        return
    if root.data == value:
        print("Element Found", end="\n")
        return
    if value < root.data:
        search(root.left, value)
    else:
        search(root.right, value)

def inorder(root):
    if (root != None):
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# for first time insertion
root = insert(None, 40)

# normal insertion
root = insert(root, 12)
root = insert(root, 45)
root = insert(root, 45)
root = insert(root, 55)
root = insert(root, 5)

# print in increasing order
inorder(root)

# searching
search(root, 2)