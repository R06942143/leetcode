class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            temp = 0
            for j in range(i):
                temp += dp[j] * dp[i - j - 1]
            dp[i] = temp
        return dp[-1]
