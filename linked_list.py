class Node:
    """Represent a single node in a singly linked list."""

    def __init__(self, data):
        """Initialize a node with data and no next node."""
        self.data = data
        self.next = None


class LinkedList:
    """Represent a singly linked list."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def append(self, data):
        """Add a new node containing data to the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def prepend(self, data):
        """Add a new node containing data to the beginning of the list."""
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete the first node containing the given data."""
        if self.head is None:
            return

        # If the head contains the data
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return

            current = current.next

    def display(self):
        """Print all elements in the linked list."""
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def to_list(self):
        """Convert the linked list into a standard Python list."""
        result = []
        current = self.head

        while current is not None:
            result.append(current.data)
            current = current.next

        return result





if __name__ == "__main__":
    my_list = LinkedList()

    my_list.append(10)
    my_list.append(20)
    my_list.append(30)

    my_list.prepend(5)

    my_list.display()
    print(my_list.to_list())

    my_list.delete(20)

    my_list.display()
    print(my_list.to_list())