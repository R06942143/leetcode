class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        def recursive(node, lr, len_):
            result.append(len_)

            if node.left is None and node.right is None:
                return

            if lr == "l":
                if node.left is not None:
                    recursive(node.left, "l", 1)
                if node.right is not None:
                    recursive(node.right, "r", len_ + 1)

            elif lr == "r":
                if node.left is not None:
                    recursive(node.left, "l", len_ + 1)
                if node.right is not None:
                    recursive(node.right, "r", 1)

        result = []
        if root.left is not None:
            recursive(root.left, "l", 1)
        if root.right is not None:
            recursive(root.right, "r", 1)
        if len(result) != 0:
            return max(result)
        return 0
