# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        if root:
            self.helper(root, low, high)

        return self.ans

    def helper(self, node: TreeNode | None, low: int, high: int):
        if low <= node.val <= high:
            self.ans += node.val
            
            if node.left:
                self.helper(node.left, low, high)
            
            if node.right:
                self.helper(node.right, low, high)

        if node.val < low and node.right:
            self.helper(node.right, low, high)
        
        if node.val > high and node.left:
            self.helper(node.left, low, high)

