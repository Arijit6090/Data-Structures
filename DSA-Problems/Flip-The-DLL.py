class DoublyListNode:
    def __init__(self, val: int, prev: 'DoublyListNode' = None, next: 'DoublyListNode' = None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def flipDoublyLinkedList(self, head: 'DoublyListNode | None') -> 'DoublyListNode | None':
        # Your implementation here
        if head is None:
            return None
        curr = head
        pred = None
        while curr is not None:
            new_node = curr.next
            curr.next = pred
            if pred is not None:
                pred.prev = curr
            pred = curr
            curr = new_node
        return pred