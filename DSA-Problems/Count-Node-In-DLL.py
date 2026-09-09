class DoublyListNode:
    def __init__(self, val: int, prev: 'DoublyListNode' = None, next: 'DoublyListNode' = None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def countNodes(self, head: DoublyListNode | None) -> int:
        # Your implementation here
        count = 0
        if head is None:
            return 0
        curr = head
        if curr.next is None:
            return 1

        while curr.next is not None:
            curr = curr.next
            count += 1
        count += 1
        return count
