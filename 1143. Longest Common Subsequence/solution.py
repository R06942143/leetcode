class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            small = text2
            large = text1
        else:
            small = text1
            large = text2
        dp = [[0] * (len(large) + 1) for _ in range(len(small) + 1)]
        for i in range(1, len(small) + 1):
            for j in range(1, len(large) + 1):
                if small[i - 1] == large[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]
