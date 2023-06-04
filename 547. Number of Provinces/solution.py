class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        graph = {}
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    if i in graph:
                        graph[i].append(j)
                    else:
                        graph[i] = [j]
                    if j in graph:
                        graph[j].append(i)
                    else:
                        graph[j] = [i]

        def dfs(x):
            if x in graph:
                for connected in graph[x]:
                    if not visited[connected]:
                        visited[connected] = 1
                        dfs(connected)

        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = True
                dfs(i)

        return count
