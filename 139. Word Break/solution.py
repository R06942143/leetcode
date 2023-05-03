class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [0] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            dp[i] = s[:i] in wordDict
            if not dp[i]:
                for j in range(1, len(dp)):
                    if dp[j] and not dp[i]:
                        dp[i] = s[j:i] in wordDict
        return dp[-1]
