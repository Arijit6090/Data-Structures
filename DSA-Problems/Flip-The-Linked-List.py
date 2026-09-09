class Solution:
    def flipLinkedList(self, head):
        # Your implementation goes here.
        # Rewire the `next` pointers to reverse the order.
    # First I thought of it like bellow but it will take ahuge time complexity of O(n**2)
        # if head is None:
        #     return None
        # curr = head
        # prev = None
        # if (curr.next == None):
        #     return head
        # while curr.next is not None:
        #     prev = curr
        #     curr = curr.next
        # last = curr
        # curr = head
        # prev = None
        # while curr.next is not None:
        #     while curr.next is not None:
        #         prev = curr
        #         curr = curr.next
        #     curr.next = prev
        #     curr = head
        #     prev = None
        # head = last
        # return head
    # actual answer which I figured out later with much lesser time complexity:
        if head is None:
            return None
        curr = head
        prev = None
        while curr is not None:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node
        return prev
# Note: ListNode class is assumed to be defined elsewhere with attributes `val` and `next`.