# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode|None) -> list[int]:
        seen = {}
        if not root:
            return []
        queue = [root]
        while queue:
            
            next_queue = []
            for element in queue:
                if element.val not in seen:
                    seen[element.val] = 1
                else:
                    seen[element.val] += 1
                if element.left:
                    next_queue.append(element.left)
                if element.right:
                    next_queue.append(element.right)
            queue = next_queue
        
        ans_dict = {}
        max_value = - float("INF")
        for key, value in seen.items():
            if value > max_value:
                max_value = value
            if value not in ans_dict:
                ans_dict[value] = [key]
            else:
                ans_dict[value].append(key)
        return ans_dict[max_value]
