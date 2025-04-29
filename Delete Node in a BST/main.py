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
            if cur.right:
                cur.right.left = cur.left
                cur = cur.right
            elif cur.left:
                cur.left.right = cur.right
                cur = cur.left
            else:
                cur = None
            if prev.right == root:
                return cur
            if prev.left and  prev.left.val == key:
                prev.left = cur
            elif prev.right and prev.right.val == key:
                prev.right = cur
            return root
        if cur.val > key:
            prev, cur = cur, cur.left
        else:
            prev, cur = cur, cur.right
    return root


f = TreeNode(7, None, None)
e = TreeNode(4, None, None)
d = TreeNode(2, None, None)
c = TreeNode(6, None, f)
b = TreeNode(3, d, e)
a = TreeNode(5, b, c)


x = deleteNode(a, 3)
x
