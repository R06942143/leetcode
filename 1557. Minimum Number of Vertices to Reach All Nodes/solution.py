class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        all_set = set()
        for i in range(n):
            all_set.add(i)
        seen = set()
        for a in edges:
            seen.add(a[1])

        return list(all_set.difference(seen))
