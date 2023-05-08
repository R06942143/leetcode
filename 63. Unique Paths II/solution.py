class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    if obstacleGrid[i][j] == 0:
                        dp[0][j] = dp[0][j - 1]
                    else:
                        dp[0][j] = 0
                elif j == 0:
                    if obstacleGrid[i][j] == 0:
                        dp[i][0] = dp[i-1][0]
                    else:
                        dp[i][0] = 0
                else:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i][j-1] + dp[i-1][j]
                    else:
                        dp[i][j] = 0
        return dp[-1][-1]