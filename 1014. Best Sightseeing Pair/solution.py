class Solution:
    def maxScoreSightseeingPair(self, A):
        cur = res = 0
        for a in A:
            res = max(res, cur + a)
            cur = max(cur, a) - 1
        return res
