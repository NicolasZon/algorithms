"""
Return the root node of a binary search tree that matches the given preorder traversal.

Recall that a binary search tree is a binary tree where for every node, any descendant of node.left
has a value < node.val, and any descendant of node.right has a value > node.val.

Also recall that a preorder traversal displays the value of the node first,
then traverses node.left, then traverses node.right.


Example :

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
"""
import math

from DataStructures.BST import print_bst


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bst_from_preorder(preorder: list, father=math.inf) -> TreeNode:
    new_node = TreeNode(preorder.pop(0))

    if len(preorder) == 0:
        return new_node

    if preorder[0] < new_node.val:
        new_node.left = bst_from_preorder(preorder, new_node.val)

    if len(preorder) == 0:
        return new_node

    elif preorder[0] < father:
        new_node.right = bst_from_preorder(preorder, father)

    return new_node


print_bst(bst_from_preorder([8, 5, 1, 7, 10, 12]))
print_bst(bst_from_preorder([10, 5, 2, 8, 15, 12, 20]))
