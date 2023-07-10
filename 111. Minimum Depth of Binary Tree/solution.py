# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        nowQueue = [root]
        ans = 0
        while nowQueue:
            ans += 1
            nextQueue = []
            for node in nowQueue:
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
                if not node.left and not node.right:
                    return ans
            nowQueue = nextQueue
        return ans
