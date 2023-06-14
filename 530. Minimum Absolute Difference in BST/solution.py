# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode | None) -> int:
        self.ans = float("INF")
        orderList = []

        def inOrder(root: TreeNode | None) -> None:
            if not root:
                return
            inOrder(root.left)
            orderList.append(root.val)
            inOrder(root.right)

        inOrder(root)
        for i in range(1, len(orderList)):
            self.ans = min(self.ans, orderList[i] - orderList[i - 1])

        return self.ans
