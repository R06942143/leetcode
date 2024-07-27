from typing import List, Tuple
import heapq

class Solution:
    def solve(self, a: int, adj: List[List[Tuple[int, int]]]) -> List[int]:
        q = [(0, a)]
        dist = [-1] * 26

        while q:
            p = heapq.heappop(q)
            for i in adj[p[1]]:
                if dist[i[0]] == -1 or p[0] + i[1] < dist[i[0]]:
                    dist[i[0]] = p[0] + i[1]
                    heapq.heappush(q, (dist[i[0]], i[0]))
        
        return dist

    def minimumCost(self, s: str, t: str, o: List[str], c: List[str], cost: List[int]) -> int:
        adj = [[] for _ in range(30)]
        n = len(o)
        for i in range(n):
            adj[ord(o[i]) - ord('a')].append((ord(c[i]) - ord('a'), cost[i]))

        m = {}
        for i in range(26):
            k = self.solve(i, adj)
            m[i] = k

        n = len(s)
        ans = 0
        for i in range(n):
            if s[i] != t[i]:
                k = m[ord(s[i]) - ord('a')][ord(t[i]) - ord('a')]
                if k == -1:
                    return -1
                ans += k

        return ans
