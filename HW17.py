#1
class Node:
    def __init__(self, data=None):
        self.data = data          # Store data in the node
        self.next = None          # Initialize the next pointer to None (for linking nodes)

class Stack:
    def __init__(self):
        self.top_node = None      # Points to the top node in the stack
        self.length = 0           # Keeps track of the number of elements in the stack

    def empty(self):
        return self.length == 0   # Checks if the stack is empty by comparing length to 0

    def size(self):
        return self.length        # Returns the current size of the stack

    def push(self, data):
        new_node = Node(data)         # Create a new node with the given data
        new_node.next = self.top_node # Link new node to the current top node
        self.top_node = new_node      # Update the top node to the new node
        self.length += 1              # Increment the stack size

    def pop(self):
        if not self.empty():              # Check if the stack is not empty
            popped_item = self.top_node.data   # Get data from the top node (node to be popped)
            self.top_node = self.top_node.next # Update top to point to the next node
            self.length -= 1                   # Decrement the stack size
            return popped_item                 # Return the data of the popped node
        else:
            raise IndexError("Stack is empty") # Raise an error if pop is attempted on an empty stack

# Initialize an empty stack
stack = Stack()

print(stack.empty())  # Check if stack is empty
print(stack.length)   # Display current length of stack

# Push several items onto the stack
stack.push(200)
stack.push(50)
stack.push(75)
stack.push(25)
stack.push(30)

print(stack.empty())  # Check if stack is still empty after pushing items
print(stack.length)   # Display updated length

# Pop items from the stack and display the resulting length and empty status
print(stack.pop())
print(stack.empty())
print(stack.length)
print(stack.pop())
print(stack.length)
print(stack.pop())
print(stack.length)
print(stack.pop())
print(stack.length)
print(stack.pop())
print(stack.empty())
print(stack.length)

# Attempting to pop from an empty stack; raises an error
print(stack.pop())
