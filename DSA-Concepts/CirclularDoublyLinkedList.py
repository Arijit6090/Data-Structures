class Node:
    def __init__(self, value = None):
        self.data = value
        self.next = None
        self.prev = None

# creation 
class CircularDLL:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        temp = Node(value)
        # in case of empty list
        if (self.head == None):
            self.head = temp
            temp.next = self.head
            temp.prev = self.head
            return

        # find the last node
        last = self.head.prev

        temp.prev = last
        temp.next = self.head

        last.next = temp
        self.head.prev = temp

    def insertAtBeg(self, value):
        temp = Node(value)
        # in case of empty list
        if (self.head == None):
            self.head = temp
            temp.next = self.head
            temp.prev = self.head
            return

        last = self.head.prev

        temp.next = self.head
        temp.prev = last

        self.head.prev = temp
        last.next = temp

        self.head = temp

    def insertAfter(self, value, x): # x is the node who behaves like position 
        temp = Node(value)
        t = self.head
        if(self.head == None):
            print("The list is empty")
            return
        # searching for the targeted node
        while(True): # using true instead of t.next != self.head so it will check the last element also
            if(t.data == x):
                temp.next = t.next
                temp.prev = t

                t.next.prev = temp
                t.next = temp
                return
            t = t.next

            if(t == self.head):
                print("There is no such element in the list")
                return

    def deletionCDLL(self, value):
        # if the list is empty
        if(self.head == None):
            print("Linked List is empty")
            return

        # if the list only contains one node
        if(self.head.next == self.head):
            if(self.head.data == value):
                self.head = None
            else:
                print("please give a valid node which exists in the list")
            return

        # if the head needs to be deleted
        if (self.head.data == value):
            last = self.head.prev

            self.head = self.head.next

            self.head.prev = last
            last.next = self.head
            return

        # for any other nodes to be deleted
        t = self.head.next

        while(t != self.head):
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            t = t.next
        print("there is no such element in the list")  

    # Print the circular doubly linked list
    def printCDLL(self):
        if(self.head == None):
            print("Circular Doubly Linked List is empty")
            return

        t = self.head

        while(t.next != self.head):
            print(t.data, end=" <--> ")
            t = t.next

        print(t.data, end = " -> repeat\n")


obj = CircularDLL()
obj.printCDLL()

obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.printCDLL()

obj.insertAtBeg(5)
obj.printCDLL()

obj.insertAfter(50, 20)
obj.printCDLL()

obj.deletionCDLL(5)
obj.printCDLL()

obj.deletionCDLL(50)
obj.printCDLL()

obj.deletionCDLL(40)
obj.printCDLL()