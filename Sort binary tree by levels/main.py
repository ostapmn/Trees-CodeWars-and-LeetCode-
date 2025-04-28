"""Module to sort a binary tree by levels."""


from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node: Node):
    if not node:
        return []
    res = []
    stack = deque()
    stack.append(node.left)
    stack.append(node.right)
    res.append(node.value)
    while True:
        if len(stack) == 0:
            return res
        node = stack.popleft()
        if not node:
            continue
        res.append(node.value)
        stack.append(node.left)
        stack.append(node.right)


k = Node(None, None, 4)
d = Node(None, None, 1)
e = Node(None, None, 3)
f = Node(None, None, 5)
c = Node(k, f, 9)
b = Node(d, e, 8)
a = Node(b, c, 2)

print(tree_by_levels(a))
