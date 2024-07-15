# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        val_to_node, kids = {}, set()
        for parent, kid, left in descriptions:
            kids.add(kid)
            parent_node = val_to_node.setdefault(parent, TreeNode(parent))
            kid_node = val_to_node.setdefault(kid, TreeNode(kid))
            if left == 1:
                parent_node.left = kid_node
            else:
                parent_node.right = kid_node
        return val_to_node[(val_to_node.keys() - kids).pop()]