class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def hasCycle(head: Node) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


A = Node("a")
B = Node("b")
C = Node("c")
D = Node("d")
E = Node("e")
F = Node("f")

if __name__ == "__main__":
    A.next, B.next, C.next = B, C, D
    print(hasCycle(A))

    A.next, B.next, C.next, D.next, E.next, F.next = B, C, D, E, F, C
    print(hasCycle(A))
