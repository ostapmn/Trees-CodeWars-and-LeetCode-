"""Delete node in Binary Search Tree"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"


def deleteNode(root:TreeNode, key: int) -> TreeNode:
    cur = root
    prev = TreeNode('None', None, root)
    while True:
        if cur is None:
            break
        if cur.val == key:
            predecessor = find_predecessor(cur) #test 1 -> 2
            predecessor.right = cur.right
            if prev.left and prev.left.val == key:
                if predecessor == cur:
                    prev.left = cur.right
                else:
                    prev.left = cur.left
            elif prev.right and prev.right.val == key:
                if predecessor == cur:
                    prev.right = cur.right
                else:
                    prev.right = cur.left
            if cur == root:
                if predecessor == cur:
                    return cur.right
                return cur.left
            return root
        if cur.val > key:
            prev, cur = cur, cur.left
        else:
            prev, cur = cur, cur.right
    return root


def find_predecessor(node: TreeNode):
    if not node.left:
        return node
    node = node.left
    while node.right:
        node = node.right
    return node

# f = TreeNode(9, None, None)
# e = TreeNode(5, None, None)
# d = TreeNode(8, None, f)
# c = TreeNode(6, e, None)
b = TreeNode(2, None, None)
a = TreeNode(1, None, b)


x = deleteNode(a, 1)
x
# print(find_predecessor(a))