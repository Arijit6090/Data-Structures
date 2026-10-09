
from collections import deque

print(" AAM ZINDEGI \n")
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enQueue(self, value):
        self.items.append(value)
        print(value, "has been inserted")

    def deQueue(self):
        if (self.isEmpty()):
            print("The Queue is currently empty. No deletion possible. Please insert some elements")
            return None

        # O(n) because elements need to be shifted
        return self.items.pop(0)

q = Queue()

print(q.isEmpty()) # True

q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)

print(q.isEmpty()) # False

print(q.deQueue()) # 10
print(q.deQueue()) # 20 
print(q.deQueue()) # 30
print(q.deQueue()) # 40

print(q.deQueue()) # The Queue is currently empty. No deletion possible. Please insert some elements

# BETTER APPROACH

print("\n MENTOS ZINDEGI \n")

class QueueBetter:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)
        print(value, "has been inserted")

    def dequeue(self):
        if self.is_empty():
            print("The Queue is currently empty. No deletion possible. Please insert some elements")
            return None

        # O(1)
        return self.items.popleft()


qnew = QueueBetter()

print(qnew.is_empty())  # True

qnew.enqueue(10)
qnew.enqueue(20)
qnew.enqueue(30)
qnew.enqueue(40)

print(qnew.is_empty())  # False

print(qnew.dequeue())  # 10
print(qnew.dequeue())  # 20
print(qnew.dequeue())  # 30
print(qnew.dequeue())  # 40

print(qnew.dequeue())  # Queue is empty...
