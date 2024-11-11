# #1
# class Node:
#     def __init__(self, data=None):
#         self.data = data          # Okay so this stores data in the node
#         self.next = None          # While this one initializes the next pointer to None
#
# class Stack:
#     def __init__(self):
#         self.top_node = None      # Top mode that is in the stack it points to that one
#         self.length = 0           # Keeps track of the number of elements in the stack
#
#     def empty(self):
#         return self.length == 0   # Checks if the stack is empty by comparing length to 0
#
#     def size(self):
#         return self.length        # size of the stack returned
#
#     def push(self, data):
#         new_node = Node(data)         # Creates a new node with the given data
#         new_node.next = self.top_node # Links new node to the current top node
#         self.top_node = new_node      # Updates the top node to the new node
#         self.length += 1              # Increments the stack size
#
#     def pop(self):
#         if not self.empty():              # With this we are checking emptiness of the stack
#             popped_item = self.top_node.data   # Getting data from the top node
#             self.top_node = self.top_node.next # Updates top to point to the next node
#             self.length -= 1                   # Decrements the stack size
#             return popped_item                 # Return the data of the popped node
#         else:
#             raise IndexError("Stack is empty") # Throws error it something goes wrong
#
#
# stack = Stack() #Nothing special here just empty stack
#
# print(stack.empty())  # Check if stack is empty
# print(stack.length)   # Display current length of stack
#
#
# stack.push(200)
# stack.push(50)
# stack.push(75)
# stack.push(25)
# stack.push(30)
#
# print(stack.empty())  # Check if stack is still empty after pushing items
# print(stack.length)   # Display updated length
#
#
# print(stack.pop())
# print(stack.empty())
# print(stack.length)
# print(stack.pop())
# print(stack.length)
# print(stack.pop())
# print(stack.length)
# print(stack.pop())
# print(stack.length)
# print(stack.pop())
# print(stack.empty())
# print(stack.length)
#
# # Attempting to pop from an empty stack; raises an error
# print(stack.pop())

#2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        position = 0
        while current and position < index - 1:
            current = current.next
            position += 1

        if current:
            new_node.next = current.next
            current.next = new_node
        else:
            print("Index out of bounds")

    def delete_by_value(self, value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            return

        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

        print("Value not found in the list")

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert_at_index(0, 10)
ll.insert_at_index(1, 20)
ll.insert_at_index(2, 30)

print("List after insertions:")
ll.print_list()

ll.delete_by_value(20)

print("List after deletion:")
ll.print_list()














