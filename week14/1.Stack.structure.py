class Node:
    def __init__(self, data, next=None):
        self.data = data  
        self.next = next  

class Stack:
    def __init__(self):
        self.top = None  

    def push(self, data):
        """Pushes a new node onto the stack (adds to the top)."""
        new_node = Node(data)
        new_node.next = self.top  
        self.top = new_node  

    def pop(self):
        """Pops the top node from the stack and returns its value."""
        if self.top is None:
            print("The stack is empty.")
            return None
        popped_node = self.top
        self.top = self.top.next  
        return popped_node.data  

    def print_stack(self):
        """Prints all elements in the stack."""
        if self.top is None:
            print("The stack is empty.")
            return
        current = self.top
        while current:
            print(current.data)
            current = current.next


stack = Stack()


stack.push("First Element")
stack.push("Second Element")
stack.push("Third Element")


print("Stack contents after pushing elements:")
stack.print_stack()


print("\nPopped element:", stack.pop())


print("\nStack contents after popping an element:")
stack.print_stack()


print("\nPopped element:", stack.pop())
print("Popped element:", stack.pop())


print("\nPopped element:", stack.pop())

