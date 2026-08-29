class Node:
    def __init__(self, info, next = None):
        self.data = info
        self.next = next

class CircularLL:
    def __init__(self, head = None):
            self.head = head

    # insert a new node at the end where the list completes one circle, example 10 20 30 again 10 will come because of circular structure then the new value will be inserted after 30
    def insertAtEnd(self, value):
        temp = Node(value)

        # if the list is empty
        if(self.head == None):
            self.head = temp
            temp.next = self.head
            return

        t = self.head

        # find the last node
        while (t.next != self.head):
            t = t.next
        t.next = temp
        temp.next = self.head

    # insert a new node at the beginning of the list, the new value node will point to the first node of the list and the last node of the list will point to the new value node
    def insertAtBeg(self, value):
        temp = Node(value)
        
        # if the list is empty
        if(self.head == None):
            self.head = temp
            temp.next = self.head
            return
        
        t = self.head

        # find the last node
        while (t.next != self.head):
            t = t.next
        temp.next = self.head
        t.next = temp
        self.head = temp

    # Insert a new node after the node containing x
    def insertAfter(self, value, x): # x is the value of the target node
        # if the list is empty
        if (self.head == None):
            print("the list is empty please insert some value with insertAtBeg or insertAtEnd methods")
            return

        temp = Node(value)
        t = self.head

        # Traversing through the list if the target node is the first node
        while (True): # it will check the last node to unlike t.next != self.head
            # if the target node is the first node
            if (t.data == x):
                temp.next = t.next
                t.next = temp
                return
            t = t.next
            if (t == self.head):
                print("there is no such element in the list")
                return

    # Deletion of the node in the list via given value
    def deletionCLL(self, value):
        # if the list is empty
        if(self.head == None):
            print("The list is already empty")
            return

        # if there is only one node
        if(self.head.next == self.head):
            if(self.head.data == value):
                self.head = None
            else:
                print("please give value that is present in the linked list")
            return

        # if there is multiple node
        # if the first node needs to be deleted
        if(self.head.data == value):
            t = self.head
            # Find the last node
            while(t.next != self.head):
                t = t.next
            self.head = self.head.next
            t.next = self.head 
            return

        # deleting any other node
        prev = self.head
        t = self.head.next

        while (t != self.head):
            if (t.data == value):
                prev.next = t.next
                return
            prev = t
            t = t.next

    # Print the circular linked list
    def printCLL(self):
        if(self.head == None):
            print("Circular Linked List is empty")
            return

        t = self.head

        while(t.next != self.head):
            print(t.data, end=" -> ")
            t = t.next

        print(t.data, end = " -> repeat\n")



# Testing of the linked list implementation
obj = CircularLL()

# insertion of nodes at the end of the linked list
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.printCLL() 

# insertion of nodes at the beginning of the linked list
obj.insertAtBeg(3)
obj.insertAtBeg(5)
obj.printCLL() 

# insertion of nodes in the middle of the linked list
obj.insertAfter(15, 10)
obj.printCLL() 

# deletion of a node from the linked list
obj.deletionCLL(30)
obj.printCLL() 

# Print the linked list
obj.printCLL() 





