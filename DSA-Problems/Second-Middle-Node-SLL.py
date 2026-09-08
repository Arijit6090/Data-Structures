# Given the head of a singly linked list, return the middle node of the list.

# - If the list contains an odd number of nodes, there is a single middle node; return that node.
# - If the list contains an even number of nodes, there are two middle nodes; return the second one (the one that appears later in the list).

# ### Example

# ```
# Input: 1 → 2 → 3 → 4 → 5
# Output: Node with value 3
# Explanation: The list has 5 nodes, so the middle node is the 3rd node, which holds the value 3.
# ```

# ### Example

# ```
# Input: 10 → 20 → 30 → 40 → 50 → 60
# Output: Node with value 40
# Explanation: The list has 6 nodes. The two middle nodes are 30 and 40; according to the rule we return the second middle node, which holds the value 40.
# ```

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        if head is None:
            return None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

# another approach:
class Solution:
    def middleNode(self, head):
        if head is None:
            return None
        current = head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        current = head

        middle = count//2
        for i in range(middle):
            current = current.next
        return current