from collections import defaultdict
class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        connect_map = defaultdict(dict)
        for u, v in connections:
            connect_map[u][v] = connect_map[v][u] = 1
        visited = [0] * n
        def dfs(node):
            if visited[node]:
                return 0
            visited[node] = 1
            for neighbor in connect_map[node]:
                dfs(neighbor)
            return 1

        return sum(dfs(node) for node in range(n)) - 1
