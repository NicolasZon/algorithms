
class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_bst(root: TreeNode):
    s = [(root, 0)]
    while s:
        node, depth = s.pop(0)
        print(node.val, end=' ')
        if node.left is None and node.right is None:
            continue
        s.append((TreeNode("X") if node.left is None else node.left, depth + 1))
        s.append((TreeNode("X") if node.right is None else node.right, depth + 1))
    print()
