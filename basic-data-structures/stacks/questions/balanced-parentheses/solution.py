def is_balanced(expr) -> bool:
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}

    for char in expr:
        if char in pairs.values():  # opening
            stack.append(char)
        elif char in pairs.keys():  # closing
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack


print(is_balanced("([{}])"))  # True
print(is_balanced("([{}{()}])"))  # True
print(is_balanced("([)]"))  # False
