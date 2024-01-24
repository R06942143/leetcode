# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0
    
    def pseudoPalindromicPaths (self, root: TreeNode | None) -> int:
        if not root:
            return self.ans

        def dfs(root: TreeNode | None, path) -> None:
            if root.val in path:
                path.remove(root.val)
            else:
                path.add(root.val)

            if not root.left and not root.right:
                if len(path) == 1 or  len(path) == 0:
                    self.ans += 1
                return

            if root.left:
                new_path = path.copy()
                dfs(root.left, new_path)

            if root.right:
                new_path = path.copy()
                dfs(root.right, new_path)

        dfs(root, set([]))

        return self.ans

