class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [0] * arrLen
        dp[0] = 1
        for i in range(steps):
            dp_next = [0] * arrLen
            for j in range(arrLen):
                if j == 0:
                    dp_next[j] = (dp[j] + dp[j + 1]) % 1000000007
                elif j == arrLen -1:
                    dp_next[j] = (dp[j - 1] + dp[j]) % 1000000007
                else:
                    dp_next[j] = (dp[j-1] + dp[j] + dp[j + 1]) % 1000000007
            dp = dp_next
        
        return dp[0]