class Stack:
    """Implement a stack using a Python list."""

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item, or None if the stack is empty."""
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        """Return the top item without removing it, or None if empty."""
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        """Return True if the stack contains no items."""
        return len(self.items) == 0


class Queue:
    """Implement a queue using a Python list."""

    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the first item, or None if the queue is empty."""
        if self.is_empty():
            return None

        return self.items.pop(0)

    def peek(self):
        """Return the first item without removing it, or None if empty."""
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        """Return True if the queue contains no items."""
        return len(self.items) == 0


def reverse_string(text):
    """Reverse a string using a Stack."""
    stack = Stack()

    for char in text:
        stack.push(char)

    reversed_text = ""

    while not stack.is_empty():
        reversed_text += stack.pop()

    return reversed_text


if __name__ == "__main__":

    # Test Stack
    stack = Stack()

    stack.push("A")
    stack.push("B")
    stack.push("C")

    print("Stack:")
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("Pop:", stack.pop())
    print("Is empty:", stack.is_empty())

    # Test Queue
    queue = Queue()

    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    print("\nQueue:")
    print("Peek:", queue.peek())
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())
    print("Is empty:", queue.is_empty())

    # Test reverse_string
    print("\nReverse string:")
    print(reverse_string("Python"))