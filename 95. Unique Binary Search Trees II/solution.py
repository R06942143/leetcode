# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        def dfs(nums):
            if not nums:
                return [None]

            answer = []

            for i in range(len(nums)):
                leftTrees = dfs(nums[:i])
                rightTrees = dfs(nums[i + 1 :])

                for l in leftTrees:
                    for r in rightTrees:
                        root = TreeNode(nums[i])
                        root.left = l
                        root.right = r
                        answer.append(root)

            return answer

        return dfs(list(range(1, n + 1)))
