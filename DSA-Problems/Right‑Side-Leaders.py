# Finding the Right Side Leaders
# Given an array **arr** of length **n**, identify all *leaders* in the array. An element is called a leader if it is greater than or equal to every element that appears to its right. The rightmost element is always a leader because there are no elements after it.

# **Input**: An array `arr[]`.

# **Output**: A list of all leaders in the order they appear in the array.

# ```
# Input: arr = [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2]
# Explanation: 17 is greater than all elements to its right [4, 3, 5, 2]; 5 is greater than the element to its right [2]; 2 has no elements to its right.
# ```
class Solution:
    def findLeaders(self, arr):
        leaders = []
    
        max_right = arr[-1] # the right most element of the list
        leaders.append(arr[-1]) # the right most element always stays at the leader

        for i in range(len(arr) - 2, -1, -1): # start at the second last element, stops at 0th index excluding -1, step by 1 right to left
            if arr[i] >= max_right:
                leaders.append(arr[i])
                max_right = arr[i]

        leaders.reverse()

        return leaders

rl = Solution()

print(rl.findLeaders([16,17,4,3,5,2]))

# Understanding with the help of linked list
# class Node:
#     def __init__(self, info, next = None):
#         self.data = info
#         self.next = next

# class SinglyLinkedList:
#     def __init__(self, head = None):
#         self.head = head
    
#     def insertAtEnd(self, value):
#         temp = Node(value)
#         if(self.head != None):
#             t1 = self.head
#             while(t1.next != None):
#                 t1 = t1.next
#             t1.next = temp
#         else: 
#             self.head = temp 

#     def insertAtBeginning(self, value):
#         temp = Node(value)
#         temp.next = self.head
#         self.head = temp

#     def insertInMiddle(self, value, position):
#         temp = Node(value)
#         t1 = self.head
#         while(t1 != None): 
#             if(t1.data == position):
#                 temp.next = t1.next
#                 t1.next = temp
#                 return
#             t1 = t1.next

#     def deleteLL(self, value):
#         if(self.head == None):
#             print("The list is already empty")
#             return
#         t1 = self.head
#         prev = t1
#         if(t1.data == value):
#             self.head = t1.next
#             return
#         while(t1 != None): 
#             if(t1.data == value):
#                 prev.next = t1.next
#                 return
            
#             prev = t1
#             t1 = t1.next

#     def printLL(self):
#         if(self.head == None):
#             print("Linked List is empty")
#             return
#         t1 = self.head
#         while(t1.next != None):
#             print(t1.data, end = " -> ")
#             t1 = t1.next
#         print(t1.data, end = " -> None\n")

#     def printRL(self):
#         if(self.head == None):
#             print("Linked List is empty")
#             return
#         t1 = self.head
#         rl = []
#         while(t1.next != None):
#             if (t1.next.data > t1.data):
#                 rl.append(t1.next.data)
#             t1 = t1.next
#         rl.append(t1.data)
#         print(rl)

# obj = SinglyLinkedList()

# obj.insertAtEnd(16)
# obj.insertAtEnd(17)
# obj.insertAtEnd(4)
# obj.insertAtEnd(3)
# obj.insertAtEnd(5)
# obj.insertAtEnd(2)

# obj.printLL()
# obj.printRL()
