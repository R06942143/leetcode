# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode|None, target: int) -> TreeNode|None:
        deleted = self.deleteLeafNodes(root, target)
        if deleted:
            return root.left
        return root
            

    def deleteLeafNodes(self, root: TreeNode|None, target: int) -> bool:
        if root.left:
            deleted = self.deleteLeafNodes(root.left, target)
            if deleted:
                root.left = None
                delete = False
        
        if root.right:
            deleted = self.deleteLeafNodes(root.right, target)
            if deleted:
                root.right = None
                delete = False

        if not root.left and not root.right and root.val == target:
            return True
        return False