# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode|None) -> bool:
        if not root:
            return True
        
        queue = [root]
        times = 0
        while queue:
            tmp = None
            times += 1
            next_queue = []
            for node in queue:
                if times % 2 == 1:
                    if node.val % 2 == 0:
                        return False
                else:
                    if node.val % 2 == 1:
                        return False
                if tmp:
                    if times % 2 == 1:
                        if node.val <= tmp:
                            return False
                    else:
                        if node.val >= tmp:
                            return False
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                tmp = node.val
            queue = next_queue
        
        return True
                            