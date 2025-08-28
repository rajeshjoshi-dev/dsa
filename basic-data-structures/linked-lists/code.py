# Implementation in Python (Singly Linked List)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Traversal
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 2. Insertion at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 3. Insertion at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # 4. Insertion after a node
    def insert_after(self, prev_node: Node, data):
        if not prev_node:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # 5. Deletion by data
    def delete_node(self, data):
        temp = self.head

        if temp.data == data:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next

        if not temp:
            return

        prev.next = temp.next

ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.print_list()   # 1 -> 2 -> 3 -> None
ll.insert_at_beginning(0)
ll.print_list()   # 0 -> 1 -> 2 -> 3 -> None

ll.delete_node(2)
ll.print_list()   # 0 -> 1 -> 3 -> None
