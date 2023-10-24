# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode|None) -> list[int]:
        ans = []
        if not root:
            return ans
        now = [root]

        while now:
            next_row = []
            max_node = -float("INF")
            for node in now:
                if node.val > max_node:
                    max_node = node.val
                if node.left:
                    next_row.append(node.left)
                if node.right:
                    next_row.append(node.right)
            ans.append(max_node)
            now = next_row

        return ans