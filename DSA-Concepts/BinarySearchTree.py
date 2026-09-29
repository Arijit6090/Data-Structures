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

# Code for getting Inorder Successor
def get_successor(root):
    root = root.right
    while(root != None and root.left != None):
        root = root.left
    return root

def delete(root, value):
    if root == None:
        return root
    elif value < root.data:
        root.left = delete(root.left, value)
    elif value > root.data:
        root.right = delete(root.right, value)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            succ = get_successor(root)
            root.data = succ.data
            root.right = delete(root.right, succ.data)
    return root


def inorder(root):
    if (root != None):
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# for first time insertion
root = insert(None, 10)

# normal insertion
root = insert(root, 8)
root = insert(root, 30)
root = insert(root, 9)
root = insert(root, 6)
root = insert(root, 25)
root = insert(root, 20)
root = insert(root, 35)
root = insert(root, 32)
root = insert(root, 50)
root = insert(root, 40)

print("\n")
# print in increasing order
inorder(root)

print("\n")
# searching
search(root, 2)

print("\n")
# deletion
delete(root, 30)
inorder(root)
print("\n")

delete(root, 32)
inorder(root)
print("\n")

delete(root, 6)
inorder(root)
print("\n")