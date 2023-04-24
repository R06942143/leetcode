class Solution:
    def fib(self, n: int) -> int:
        if not n:
            return 0
        dp = [0 for i in range(n)]
        dp[0] = 1
        if n == 1:
            return dp[0]
        dp[1] = 1
        if n - 1 < 2:
            return dp[n - 1]
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]
