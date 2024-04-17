# Definition for a binary tree node.
import string


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode | None) -> str:
        self.ans = None
        self.letterMap = {}
        lowers = list(string.ascii_lowercase)
        for x in range(len(lowers)):
            self.letterMap[x]=lowers[x]


        def dfs(root, current_str) -> None:
            current_str = self.letterMap[root.val] + current_str

            if root.left:
                dfs(root.left, current_str)
            
            if root.right:
                dfs(root.right, current_str)
            
            if not root.left and not root.right:
                if not self.ans:
                    self.ans = current_str
                else:
                    self.ans = min(self.ans, current_str)
        
        dfs(root, "")

        return self.ans