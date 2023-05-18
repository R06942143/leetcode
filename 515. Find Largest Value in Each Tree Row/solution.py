# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: TreeNode|None) -> list[int]:
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            new_queue = []
            largest = float("-inf")
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
                if node.val > largest:
                    largest = node.val
            ans.append(largest)
            queue = new_queue
        return ans