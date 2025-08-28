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

    def zipper(self, node2: Node): ...

    def recursive_zipper(self, node2: Node): ...

    def __recursive_zipper(self, node2: Node): ...


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

ll1.zipper(ll2)
ll1.print_list()  # 'a' -> 'q' -> 'b' -> 'r' -> 'c' > 'd' -> 'e' -> 'f' -> None
