class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def reverse(self):
        temp = self.head

        if not temp or not temp.next:
            return

        prev = None
        while temp:
            _ = temp.next
            temp.next = prev

            prev = temp
            temp = _

        self.head = prev

    def recursively_reverse(self):
        head = self.__recursively_reverse(self.head)
        self.head = head

    def __recursively_reverse(self, node: Node = None, prev: Node = None):
        if not node:
            return prev

        _ = node.next
        node.next = prev

        return self.__recursively_reverse(_, node)


ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.print_list()  # 1 -> 2 -> 3 > 4 -> None

ll.reverse()
ll.print_list()  # 4 -> 3 -> 2 -> 1 -> None

ll.recursively_reverse()
ll.print_list()  # 1 -> 2 -> 3 -> 4 -> None
