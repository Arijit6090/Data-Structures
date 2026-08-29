# This is the the node structure and created object for doubly linked list, where each node has three attributes: data, next, and prev. The data attribute stores the value of the node, the next attribute points to the next node in the linked list, and the prev attribute points to the previous node in the linked list. If there is no next or previous node, they will be set to None.
class Node:
    def __init__(self, value = None):
        self.data = value
        self.next = None
        self.prev = None

# This is the object for DoublyLL where this class defines the doubly linked list and its operations. It has one attribute, head, which points to the first node in the doubly linked list. If the doubly linked list is empty, head will be set to None.
class DoublyLL:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the end of the doubly linked list. It takes a value as input, creates a new node with that value, and appends it to the end of the doubly linked list. If the doubly linked list is empty, it sets the head to the new node.
    def insertAtEnd(self, value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp
            return
        t = self.head
        while(t.next != None):
            t = t.next
        t.next = temp
        temp.prev = t

    # Function to insert a new node at the beginning of the doubly linked list. It takes a value as input, creates a new node with that value, and sets it as the new head of the doubly linked list. The next attribute of the new node points to the previous head node, and the prev attribute of the previous head node points back to the new node.
    def insertAtBeg(self, value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    # Function to insert a new node at the middle of the doubly linked list. It takes a value as input, creates a new node with that value, and inserts it after the node with the specified value.
    def insertAtMid(self, value, x): # x is the positon
        temp = Node(value)
        t = self.head
        while(t != None): #can be t.next != None
            if(t.data == x):
                temp.next = t.next
                if(t.next != None):
                    t.next.prev = temp
                t.next = temp
                temp.prev = t
                return
            else:
                t = t.next

    # Function to delete a node from the doubly linked list. It takes a value as input and removes the first occurrence of that value from the doubly linked list. If the value is not found, no changes are made to the doubly linked list.
    def deletionDll(self, value):
        if(self.head == None):
            print("Linked List is empty")
            return
        t = self.head
        if(t.data == value):
            self.head = t.next
            if (self.head != None):
                self.head.prev = None
            return
        while(t.next != None):
            if (t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next
        if (t.data == value):
            t.prev.next = None

    # Function to print the doubly linked list. It traverses the doubly linked list starting from the head and prints the data of each node followed by a double arrow (<-->) to indicate the link to the next node. When it reaches the end of the doubly linked list, it prints "None" to indicate that there are no more nodes.
    def printDLL(self):
            if(self.head == None):
                print("Linked List is empty")
                return
            t = self.head
            while(t.next != None):
                print(t.data, end = " <--> ")
                t = t.next
            print(t.data, end = " <--> None\n")

obj = DoublyLL()
obj.printDLL()

obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.printDLL()

obj.insertAtBeg(5)
obj.printDLL()

obj.insertAtMid(50, 20)
obj.printDLL()

obj.deletionDll(5)
obj.printDLL()

obj.deletionDll(50)
obj.printDLL()

obj.deletionDll(40)
obj.printDLL()

