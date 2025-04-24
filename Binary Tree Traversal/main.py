"""Module traversal"""

class Node:
    """Class to represent node"""
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __repr__(self):
        return f'{self.data}'


# Pre-order traversal
def pre_order(node:Node):
    """Preorder traversal"""
    if node is None:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)



# In-order traversal
def in_order(node:Node):
    """In-order traversal"""
    if node is None:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)


# Post-order traversal
def post_order(node: Node):
    """Post-order traversal"""
    if node is None:
        return []
    return post_order(node.left) + post_order(node.right) + [node.data]



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(pre_order(a))
print(post_order(a))
print(in_order(a))
