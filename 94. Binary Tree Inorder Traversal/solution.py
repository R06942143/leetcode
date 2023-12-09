# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = []

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        def inorder(node: TreeNode):
            if node.left:
                inorder(node.left)
            self.ans.append(node.val)
            if node.right:
                inorder(node.right)

        if not root:
            return self.ans

        inorder(root)
        return self.ans