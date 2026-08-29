# FIRST CODE: These operations are O(n) because Python has to shift the other elements whenever you insert/remove from index 0. 
# class Stack:
#     def __init__(self):
#         self.s = [] # creates an empty list

#     def Push(self, value):
#         self.s.insert(0, value)

#     def Peek(self):
#         if len(self.s) == 0:
#             print("The Stack is empty")
#             return
#         return self.s[0]

#     def Pop(self):
#         if len(self.s) == 0:
#             print("The Stack is empty")
#             return
#         return self.s.pop(0)

# SECOND CODE WITH O(1) TIME COMPLEXITY
class Stack:
    def __init__(self):
        self.s = [] # creates an empty list where the s is the name of the satck object

    def Push(self, value):
        self.s.append(value)

    def Peek(self):
        if len(self.s) == 0:
            print("The stack is empty")
            return
        return self.s[-1]

    def Pop(self):
        if len(self.s) == 0:
            print("The stack is empty")
            return
        return self.s.pop()