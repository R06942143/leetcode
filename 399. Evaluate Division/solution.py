class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = defaultdict(dict)
        for i in range(len(equations)):
            self.graph[equations[i][0]][equations[i][1]] = values[i]
            self.graph[equations[i][1]][equations[i][0]] = 1 / values[i]

        # @cache
        def dfs(start: str, end: str, seen: dict) -> int:
            if start == end and start in self.graph and end in self.graph:
                return 1
            seen[start] = True
            for key, value in self.graph[start].items():
                if key not in seen:
                    if key == end:
                        return value
                    else:
                        following = dfs(key, end, seen)
                        if following != -1:
                            return value*following
            return -1
        ans = []
        for item in queries:
            seen = {}
            ans.append(dfs(item[0], item[1], seen))
        return ans