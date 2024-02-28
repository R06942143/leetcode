# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        queue = [root]
        left_most_value = root.val
        while queue:
            next_queue = []
            left_most_value = queue[0].val
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        
        return left_most_value