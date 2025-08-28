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

    def find_a_node(self, target) -> bool:
        temp = self.head
        while temp:
            if not temp.next:
                return False

            if temp.data == target:
                return True

            temp = temp.next

        return False

    def recursively_find_a_node(self, target) -> bool:
        return self.__recursively_find_a_node(target, self.head)

    def __recursively_find_a_node(self, target, node: Node = None) -> bool:
        if not node:
            return False

        if node.data == target:
            return True

        return self.__recursively_find_a_node(target, node.next)


ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.print_list()  # 1 -> 2 -> 3 -> None

print(ll.find_a_node(2))  # True
print(ll.recursively_find_a_node(2))  # True

print(ll.find_a_node(9))  # False
print(ll.recursively_find_a_node(9))  # False
