class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def isPalindrome(head: Node) -> bool:
    slow = fast = head

    # Find middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # Compare halves
    left, right = head, prev
    while right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.next

    return True


A = Node("a")
B = Node("b")
C = Node("c")
c = Node("c")
b = Node("b")
a = Node("a")


if __name__ == "__main__":
    A.next, B.next, C.next, c.next, b.next, a.next = B, C, c, b, a, None
    print(isPalindrome(A))  # abccba
    A.next, B.next, C.next, b.next, a.next = B, C, b, a, None
    print(isPalindrome(A))  # abcba
    A.next, B.next, C.next, a.next = B, C, a, None
    print(isPalindrome(A))  # abca
