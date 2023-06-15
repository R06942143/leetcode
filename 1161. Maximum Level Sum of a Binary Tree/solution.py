# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        queue = [root]
        ans = 0
        count = float("-inf")
        level = 0
        while queue:
            level += 1
            tmp = 0
            new_queue = []
            for node in queue:
                tmp += node.val
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
            if tmp > count:
                count = tmp
                ans = level
        return ans
