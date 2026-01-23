class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def print_all(self):
        node = self
        while node:
            print(f"{node.data} -> ", end="")
            node = node.next
        print("None")


def removeNthFromEnd(head: Node, n: int) -> bool:
    slow = fast = head

    for _ in range(n + 1):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next


A = Node("a")
B = Node("b")
C = Node("c")
D = Node("d")
E = Node("e")
F = Node("f")


if __name__ == "__main__":
    A.next, B.next, C.next, D.next, E.next, F.next = B, C, D, E, F, None
    A.print_all()  # a -> b -> c -> d -> e -> f -> None
    removeNthFromEnd(A, 2)  # remove d
    A.print_all()  # a -> b -> c -> e -> f -> None
