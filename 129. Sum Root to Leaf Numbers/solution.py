# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        self.ans = 0

        def dfs(root: TreeNode | None, current_path) -> None:
            if root and not root.left and not root.right:
                self.ans += int(current_path + str(root.val))
            
            if root.left:
                dfs(root.left, current_path + str(root.val))
            
            if root.right:
                dfs(root.right, current_path + str(root.val))
            
        dfs(root, "")

        return self.ans