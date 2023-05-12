class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        dp = [0] * len(questions)
        dp[-1] = questions[-1][0]
        for i in range(len(questions) - 2, -1, -1):
            dp[i] = questions[i][0]
            if i + questions[i][1] + 1 < len(questions):
                dp[i] += dp[i + questions[i][1] + 1]
            dp[i] = max(dp[i], dp[i + 1])
        return dp[0]
