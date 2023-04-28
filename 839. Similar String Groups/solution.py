from collections import defaultdict


class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        UF = {}
        ranks = defaultdict(int)

        def find(x):
            if x not in UF:
                UF[x] = x
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if ranks[rootX] < ranks[rootY]:
                UF[rootX] = rootY
            else:
                UF[rootY] = rootX
                if ranks[rootX] == ranks[rootY]:
                    ranks[rootX] += 1

        def areNeighbors(a, b):
            dif = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    dif += 1
            return dif == 0 or dif == 2

        # Checking all pairs and union two nodes if they are neighbors
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if areNeighbors(strs[i], strs[j]):
                    union(strs[i], strs[j])

        # Find the number of roots in UF
        return len(set([find(x) for x in strs]))

    """
    def numSimilarGroups(self, strs: List[str]) -> int:
        @cache
        def similar(str1: str, str2: str) -> bool:
            count = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    count += 1
            return count == 2
        self.map = {}
        while strs:
            word = strs.pop()
            self.map[word] = [word]
            for i in strs:
    """
