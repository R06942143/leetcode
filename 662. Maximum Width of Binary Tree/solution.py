# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_width = 1
        queue = []
        queue.append((root, 1))
        while(queue):
            next_queue = []
            for node, index in queue:
                if node.left:
                    next_queue.append((node.left, index*2))
                if node.right:
                    next_queue.append((node.right, index*2 + 1))
            if next_queue:
                self.max_width = max(self.max_width, next_queue[-1][1] - next_queue[0][1] + 1)
            queue = next_queue
        return self.max_width