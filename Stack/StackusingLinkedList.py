class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None  # Initially, the stack is empty, so the top is None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  # Link the new node to the previous top
        self.top = new_node  # Update the top to the new node
        print(f"Pushed {data} onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack underflow! Cannot pop from an empty stack.")
            return None
        popped_node = self.top
        self.top = self.top.next  # Update the top to the next node
        print(f"Popped {popped_node.data} from the stack.")
        return popped_node.data

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        print(f"Top of stack is {self.top.data}")
        return self.top.data

    def display(self):
        current = self.top
        if self.is_empty():
            print("Stack is empty.")
            return
        print("Stack elements:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.peek()
