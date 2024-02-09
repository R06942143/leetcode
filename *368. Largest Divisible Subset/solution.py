class Solution:
    def largestDivisibleSubset(self, a: list[int]) -> list[int]:
        dp = {s: [s] for s in a}; a.sort()
        for i, s in enumerate(a):
            dp[s] += max([dp[a[j]] for j in range(i) if a[i] % a[j] == 0] or [[]], key=len)
        return max(dp.values() or [[]], key=lambda x: len(x))
