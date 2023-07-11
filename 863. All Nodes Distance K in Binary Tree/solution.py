# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        parent = {}
        queue = [root]
        while queue:
            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                    parent[node.left] = node
                if node.right:
                    new_queue.append(node.right)
                    parent[node.right] = node
            queue = new_queue
        queue = [target]
        visited = {target: 1}
        while queue and k > 0:
            new_queue = []
            for node in queue:
                if node.left and node.left not in visited:
                    new_queue.append(node.left)
                    visited[node.left] = 1
                if node.right and node.right not in visited:
                    new_queue.append(node.right)
                    visited[node.right] = 1
                if node in parent and parent[node] not in visited:
                    new_queue.append(parent[node])
                    visited[parent[node]] = 1
            k -= 1
            queue = new_queue
        ans = []
        for node in queue:
            ans.append(node.val)
        return ans
