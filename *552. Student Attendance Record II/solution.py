class Solution:
    def checkRecord(self, n: int) -> int:
        if not n:
            return 0

        if n == 1:
            return 3

        MOD = 10 ** 9 + 7
        dp = [1, 2, 4] + [0] * (n - 2)

        # Calculate sequences without 'A'.
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

        # Calculate final result.
        rslt = dp[n] % MOD
        for i in range(n):
            rslt += (dp[i] * dp[n - 1 - i]) % MOD

        return rslt % MOD