# This is the object for Node where this class define how a single node will look like in the linked list. It has two attributes, data and next. The data attribute stores the value of the node, while the next attribute points to the next node in the linked list. If there is no next node, it will be set to None.
class Node:
    def __init__(self, info, next = None):
        self.data = info
        self.next = next

# Object for SinglyLinkedList where this class defines the linked list and its operations. It has one attribute, head, which points to the first node in the linked list. If the linked list is empty, head will be set to None.
class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head
    
    # Function to insert a new node at the end of the linked list. It takes a value as input, creates a new node with that value, and appends it to the end of the linked list. If the linked list is empty, it sets the head to the new node.
    def insertAtEnd(self, value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else: 
            self.head = temp # if the list is empty

    # Function to insert a new node at the beginning of the linked list. It takes a value as input, creates a new node with that value, and sets it as the new head of the linked list. The next attribute of the new node points to the previous head node.
    def insertAtBeginning(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    # Function to insert a new node in the middle of the linked list. It takes a value and a position as input, creates a new node with that value, and inserts it after the node with the specified position. If the position is not found in the linked list, the new node will not be inserted.
    def insertInMiddle(self, value, position):
        temp = Node(value)
        t1 = self.head
        while(t1 != None): # can be t1.next != None
            if(t1.data == position):
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next

    # Function to delete a node from the linked list. It takes a value as input and removes the first occurrence of that value from the linked list. If the value is not found, no changes are made to the linked list.
    def deleteLL(self, value):
        if(self.head == None):
            print("The list is already empty")
            return
        t1 = self.head
        prev = t1
        if(t1.data == value):
            self.head = t1.next
            return
        while(t1 != None): # can be t1.next != None
            if(t1.data == value):
                prev.next = t1.next
                return
            
            prev = t1
            t1 = t1.next
        # if the while condition is t1.next != None then 
        # if(t1.data == value):
        #   prev.next = None

    # Function to print the linked list. It traverses the linked list starting from the head and prints the data of each node followed by an arrow (->) to indicate the link to the next node. When it reaches the end of the linked list, it prints "None" to indicate that there are no more nodes.
    def printLL(self):
        if(self.head == None):
            print("Linked List is empty")
            return
        t1 = self.head
        while(t1.next != None):
            print(t1.data, end = " -> ")
            t1 = t1.next
        print(t1.data, end = " -> None\n")


# Testing of the linked list implementation
obj = SinglyLinkedList()

# insertion of nodes at the end of the linked list
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)

# insertion of nodes at the beginning of the linked list
obj.insertAtBeginning(5)
obj.insertAtBeginning(3)

# insertion of nodes in the middle of the linked list
obj.insertInMiddle(15, 10)

# deletion of a node from the linked list
obj.deleteLL(30)

# Print the linked list
obj.printLL() 