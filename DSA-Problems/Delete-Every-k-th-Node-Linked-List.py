# Given a singly linked list, remove every **k‑th** node from the list (using 1‑based indexing). It is guaranteed that **k** is less than or equal to the length of the list. After removal, the remaining nodes should stay in their original order.

# **Example 1:**

# ```text
# Input:  List: 1 → 2 → 3 → 4 → 5 → 6,  k = 2
# Output: 1 → 3 → 5
# Explanation: Every 2nd node (2, 4, 6) is removed, leaving 1, 3, and 5.
# ```

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeEveryKthNode(self, head, k):
        if head is None:
            return None
        if k == 1:
            return None
        current = head
        prev = None
        count = 1
        while current is not None:
            if count % k == 0:
                prev.next = current.next
            else:
                prev = current
            current = current.next
            count += 1
        return head

# THIS CODE IS WRITTEN ON MASTERJI PLATFORM FOR SOLVING. THE CORE LOGIC IS FINR BUT THIS CODE WILL NOT WORK IN THE EDITOR.  