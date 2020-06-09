"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!

"""

from linked_list import Node, LinkedList

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
        
#         return self.size

#     def enqueue(self, value):
        
#         self.size += 1
#         self.storage.insert(0, value)

#     def dequeue(self):

#         if self.size == 0:

#             return None
        
#         else:
        
#             self.size -= 1
#             return self.storage.pop()

# class Queue:

#     def __init__(self):

#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):

#         return self.size

#     def enqueue(self, value):

#         self.size += 1
#         self.storage.add_in_front_of_head(value)


#     def dequeue(self):

#         if self.size == 0:

#             return None

#         else:

#             self.size -= 1
#             return self.storage.remove_tail()

class Stack:    

    def __init__(self):

        self.size = 0
        self.storage = []
        
        
    def __len__(self):
        return self.size

    def push(self, value):
        
        self.storage.append(value)
        self.size = self.size + 1

    def pop(self):

        if self.size == 0:

            return None

        else:

            self.size = self.size - 1
            return self.storage.pop()
            


class Queue:

    def __init__(self):

        self.size = 0
        self.to_add = Stack()
        self.to_remove = Stack()

    def __len__(self):

        return self.size

    def enqueue(self, value):

        self.to_add.push(value)
        self.to_remove.storage = self.to_add.storage.reverse()
        self.size += 1
        
    def dequeue(self):

        if self.size == 0:

            return None

        elif self.size == 1:

        
            value = self.to_remove.pop()
            self.to_add.storage = []
            self.size -= 1

            return value

        else: 

            value = self.to_remove.pop()
            self.to_add.storage = self.to_remove.storage.reverse()
            self.size -= 1
            
            return value









