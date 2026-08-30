from collections import deque

print(" AAM ZINDEGI \n")
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def insertAtRear(self, value):
        self.items.append(value)
        print(value, "has been inserted at the rear")

    def deleteFromFront(self):
        if (self.isEmpty()):
            print("The Queue is currently empty. No deletion possible. Please insert some elements")
            return None

        # O(n) time complexity because of shifting
        return self.items.pop(0)

    def insertAtFront(self, value):
        # O(n) time complexity because of shifting
        self.items.insert(0, value)
        print(value, "has been inserted at the front")

    def deleteFromRear(self):
        if (self.isEmpty()):
            print("The Queue is currently empty. Deletion isn't possible. Please insert some elements")
            return None

        return self.items.pop()

dq = Deque()

print(dq.isEmpty()) # True

dq.insertAtFront(10)
dq.insertAtRear(20)
dq.insertAtFront(30)
dq.insertAtFront(40)
dq.insertAtRear(50)

# The Que Should look like this
# 10
# 10 20 
# 30 10 20
# 40 30 10 20
# 40 30 10 20 50

print(dq.isEmpty()) # False

print(dq.deleteFromFront()) # 40
print(dq.deleteFromFront()) # 30
print(dq.deleteFromRear()) # 50
print(dq.deleteFromRear()) # 20

# 10 - the deque currently contains only one element
# Deleting from either front or rear would remove 10
print(dq.deleteFromFront())

print(dq.deleteFromRear()) # The Queue is currently empty. Deletion isn't possible. Please insert some elements
print(dq.deleteFromFront()) # The Queue is currently empty. No deletion possible. Please insert some elements

# BETTER APPROACH WITH O(1) TIME COMPLEXITY
# All four deque operations are O(1)

print("\n MENTOS ZINDEGI \n")

class DequeBetter:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def insert_at_rear(self, value):
        self.items.append(value)
        print(value, "has been inserted at the rear")

    def delete_from_front(self):
        if self.is_empty():
            print("The Deque is currently empty. No deletion possible.")
            return None

        # BETTER APPROACH WITH O(1) TIME COMPLEXITY 
        return self.items.popleft()

    def insert_at_front(self, value):
        self.items.appendleft(value)
        print(value, "has been inserted at the front")

    def delete_from_rear(self):
        if self.is_empty():
            print("The Deque is currently empty. No deletion possible.")
            return None

        return self.items.pop()


dq = DequeBetter()

print(dq.is_empty())  # True

dq.insert_at_front(10)
dq.insert_at_rear(20)
dq.insert_at_front(30)
dq.insert_at_front(40)
dq.insert_at_rear(50)

# Deque:
# Front → 40 30 10 20 50 ← Rear

print(dq.is_empty())  # False

print(dq.delete_from_front())  # 40
print(dq.delete_from_front())  # 30
print(dq.delete_from_rear())   # 50
print(dq.delete_from_rear())   # 20
print(dq.delete_from_front())  # 10

print(dq.delete_from_rear())   # Deque is empty
print(dq.delete_from_front())  # Deque is empty