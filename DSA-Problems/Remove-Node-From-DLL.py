class DoublyNode:
    def __init__(self, val: int, next: 'DoublyNode' = None, prev: 'DoublyNode' = None):
        self.val = val          # stored value
        self.next = next        # next node or None
        self.prev = prev        # previous node or None

class Solution:
    def deleteNode(self, head: DoublyNode | None, target: DoublyNode | None) -> DoublyNode | None:
        # Your implementation here
        if head is None:
            return None
        # if there is no target
        if target is None:
            return head
        # if the first node is target
        if target is head:
            head = target.next
            if head is not None:
                head.prev = None
        # if the target is somewgere in the middle
        else:
            target.prev.next = target.next
            # if the target is the last node
            if target.next != None:
                target.next.prev = target.prev
        # disconnecting the target
        target.next = None
        target.prev = None

        return head
