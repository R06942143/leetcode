import heapq


class Solution:
    def minFallingPathSum(self, A):
        r = [(0, -1)]
        for row in A:
            r = heapq.nsmallest(2, ((a + r[i == r[0][1]][0], i)
                                    for i, a in enumerate(row)))
        return r[0][0]