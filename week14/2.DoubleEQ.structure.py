class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data  
        self.next = next  
        self.prev = prev  

class Deque:
    def __init__(self):
        self.front = None  
        self.rear = None   
    
    def push_left(self, data):
        """Adds a new node to the front (left) of the deque."""
        new_node = Node(data, next=self.front)
        if self.front is None:  # If deque is empty
            self.rear = new_node  # The rear is also the new node
        else:
            self.front.prev = new_node  
        self.front = new_node  
    
    def push_right(self, data):
        """Adds a new node to the rear (right) of the deque."""
        new_node = Node(data, prev=self.rear)
        if self.rear is None:  
            self.front = new_node  
        else:
            self.rear.next = new_node  
        self.rear = new_node  
    
    def pop_left(self):
        """Removes and returns the node from the front (left) of the deque."""
        if self.front is None:
            print("Deque is empty.")
            return None
        value = self.front.data
        self.front = self.front.next
        if self.front is None:  
            self.rear = None  
        else:
            self.front.prev = None  
        return value
    
    def pop_right(self):
        """Removes and returns the node from the rear (right) of the deque."""
        if self.rear is None:
            print("Deque is empty.")
            return None
        value = self.rear.data
        self.rear = self.rear.prev
        if self.rear is None:  
            self.front = None  
        else:
            self.rear.next = None  
        return value
    
    def print_deque(self):
        """Prints all elements in the deque from front to rear."""
        current = self.front
        if current is None:
            print("Deque is empty.")
            return
        while current:
            print(current.data, end=" ")
            current = current.next
        print()  



deque = Deque()

# elements to the deque
deque.push_left("First Element")
deque.push_right("Second Element")
deque.push_left("Third Element")
deque.push_right("Fourth Element")

# Print the deque
print("Deque contents after pushing elements:")
deque.print_deque()

# Remove elements from the deque
print("\nPopped element from left:", deque.pop_left())
deque.print_deque()

print("\nPopped element from right:", deque.pop_right())
deque.print_deque()

# Add more elements
deque.push_left("Fifth Element")
deque.push_right("Sixth Element")
print("\nDeque contents after adding more elements:")
deque.print_deque()

# Pop all remaining elements
print("\nPopped element from left:", deque.pop_left())
print("Popped element from right:", deque.pop_right())
print("Popped element from left:", deque.pop_left())
print("Popped element from right:", deque.pop_right())

# Try to pop from an empty deque
print("\nPopped element from left:", deque.pop_left())
