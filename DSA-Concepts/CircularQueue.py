# This is the actual traditional implementation of circular queue which can be implemented in any programming language. unlike the previous stack and queue code I did not used push, pop, append, insert like inbuild functions in it.
class CircularQueue:
    # basic structure of a circular queue taking a fixed size as input parameter and initial empty queue state variables
    def __init__(self, size):
        self.size = size
        self.items = [None]*size
        self.front = self.rear = -1

    def isEmpty(self):
        # while empty, the self.front = self.rear = -1 , this functions returns boolean for conditional check
        return self.front == -1

    def isFull(self):
        # while full, the self.front = (self.rear + 1) % self.size , this functions returns boolean for conditional check
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if (self.isFull()):
            print(value, "Can't be Inserted, The Circular Queue is Full")
        # if the queue is empty, then the first element insertion occurs and both front and rear are set to 0
        elif (self.isEmpty()):
            self.front = self.rear = 0
            self.items[self.rear] = value
            print("The first element has been inserted", value)
        # if rear is at the end of the queue but there are still empty spot available in the smaller areas then the % self.size operation will adjust the rear and move it back to the 0th index
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value
            print("element inserted", value)

    def dequeue(self):
        if (self.isEmpty()):
            print("The Circular Queue is Empty")
        # if the queue currently has only one element then both the front and rear will be set to it's initial state and all the elements of the items list will be set to none
        elif (self.front == self.rear):
            print(self.items[self.front], "the last element has been dequed")
            self.items[self.front] = None
            self.front = self.rear = -1
        # the item from items list targeted by front will be returned and front will be increamented by + 1 and for the circular deletion if rear is smaller than front then the % self.size will adjust it and the front targeted element will be set to none  
        else: 
            print(self.items[self.front], "has been dequed")
            self.items[self.front] = None
            self.front = (self.front + 1) % self.size

    def printCQ(self):
        print("The current status of the queue is: ", self.items)

cq = CircularQueue(5)

cq.dequeue()

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)

cq.printCQ()

cq.dequeue()
cq.dequeue()
cq.dequeue()

cq.printCQ()

cq.enqueue(60)

cq.printCQ()

cq.dequeue()
cq.dequeue()

cq.dequeue()

cq.dequeue()
