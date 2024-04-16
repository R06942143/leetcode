# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode|None, val: int, depth: int) -> TreeNode|None:
        if not root:
            return TreeNode(val)
        
        if depth == 1:
            return TreeNode(val, left=root)
        
        queue = [root]
        curr = 1
        while queue and curr != depth - 1:
            next_queue = []
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                
                if node.right:
                    next_queue.append(node.right)
                
            queue = next_queue
            curr += 1

        for node in queue:
            node.left = TreeNode(val, left=node.left)
            node.right = TreeNode(val, right=node.right)
        
        return root
        