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

    def get_sum(self) -> int:
        total = 0
        temp = self.head
        while temp:
            total += temp.data
            temp = temp.next

        return total

    def get_recursive_sum(self) -> int:
        return self.__get_recursive_sum(self.head)

    def __get_recursive_sum(self, node: Node = None) -> int:
        if not node:
            return 0

        return node.data + self.__get_recursive_sum(node.next)


ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.print_list()  # 1 -> 2 -> 3 -> None

print(ll.get_sum())  # 6
print(ll.get_recursive_sum())  # 6

ll.insert_at_end(21)
ll.print_list()  # 0 -> 2 -> 3 -> 21 -> None

print(ll.get_sum())  # 27
print(ll.get_recursive_sum())  # 27
