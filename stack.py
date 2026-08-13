class Stack:
    """Stack class implementation"""
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    """Queue class implementation"""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0




stack = Stack()

stack.push("A")
stack.push("B")
stack.push("C")

print("Stack:")
print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Pop:", stack.pop())
print("Is empty:", stack.is_empty())




queue = Queue()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print("\nQueue:")
print("Peek:", queue.peek())
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
print("Is empty:", queue.is_empty())


def reverse_string(text):
    """Reverse a string using a Stack."""
    stack = Stack()

    for char in text:
        stack.push(char)

    reversed_text = ""

    while not stack.is_empty():
        reversed_text += stack.pop()

    print(reversed_text)

    return reversed_text



if __name__ == "__main__":
    reverse_string(text="Python")