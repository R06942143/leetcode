class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [0] * (high)
        mod = 10 ** 9 + 7
        
        for end in range(1, high + 1):
            if end >= zero:
                dp[end] += dp[end - zero]
            if end >= one:
                dp[end] += dp[end - one]
            dp[end] %= mod
        
        return sum(dp[low : high + 1]) % mod

''' TLE answer
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        ans = 0
        dp = [[0] * (high//zero + 1) for _ in range(low//one + 1)]
        for i in range(low//one + 1):
            dp[i][0] = 1
            if low <= i*one and high >= i * one:
                ans += dp[i][0]
        for j in range(high//zero + 1):
            dp[0][j] = 1
            if low <= j * zero and high >= j * zero:
                ans += dp[0][j]
        for i in range(1, low//one + 1):
            for j in range(1, high//zero + 1):
                if high >= i * one + j * zero:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                if low <= i * one + j * zero and high >= i * one + j * zero:
                    ans += dp[i][j]
        return ans % 1000000007
'''