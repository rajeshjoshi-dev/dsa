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

    def zipper_v1(self, node2: Node):
        tail = self.head
        node1: Node = self.head.next

        counter = 0
        while True:
            counter += 1

            if not node1:
                tail.next = node2
                break

            if not node2:
                tail.next = node1
                break

            if counter % 2 == 1:
                current = node2
                node2 = node2.next
            else:
                current = node1
                node1 = node1.next

            tail.next = current
            tail = current

    def zipper(self, node2: Node):
        node1 = self.head

        while True:

            n1next = node1.next
            n2next = node2.next

            node1.next = node2

            if not n1next:
                break

            node2.next = n1next

            if not n2next:
                break

            node1 = n1next
            node2 = n2next

    def recursive_zipper(self, node2: Node):
        self.__recursive_zipper(self.head, node2)

    def __recursive_zipper(self, node1: Node, node2: Node):
        if not node1 or not node2:
            return

        n1next = node1.next
        n2next = node2.next

        node1.next = node2

        if not n1next:
            return

        node2.next = n1next

        if not n2next:
            return

        self.__recursive_zipper(n1next, n2next)


ll1 = LinkedList()
ll1.insert_at_end("a")
ll1.insert_at_end("b")
ll1.insert_at_end("c")
ll1.insert_at_end("d")
ll1.insert_at_end("e")
ll1.insert_at_end("f")
ll1.print_list()  # 'a' -> 'b' -> 'c' > 'd' -> 'e' -> 'f' -> None

ll2 = LinkedList()
ll2.insert_at_end("q")
ll2.insert_at_end("r")
ll2.print_list()  # 'q' -> 'r' -> None

ll1.recursive_zipper(ll2.head)
ll1.print_list()  # 'a' -> 'q' -> 'b' -> 'r' -> 'c' > 'd' -> 'e' -> 'f' -> None
