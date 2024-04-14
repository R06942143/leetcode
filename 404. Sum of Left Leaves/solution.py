# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        self.ans = 0
        def dfs(root, is_left):
            if root.left == None and root.right == None and is_left:
                self.ans += root.val

            if root.left:
                dfs(root.left, True)
            
            if root.right:
                dfs(root.right, False)
            
        if root:
            if root.left:
                dfs(root.left, True)
            if root.right:
                dfs(root.right, False)
        
        return self.ans