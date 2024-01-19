class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        
        n = len(matrix)
        dp = matrix[0]
        
        for i in range(1,n):
            temp = dp[:]
            for j in range(n):
                if j == 0:
                    temp[j] = min(dp[j+1] + matrix[i][j], dp[j] + matrix[i][j])
                elif j == n-1:
                    temp[j] = min(dp[j] + matrix[i][j], dp[j-1] + matrix[i][j])
                else:
                    temp[j] = min(dp[j] + matrix[i][j], dp[j-1] + matrix[i][j], dp[j+1] + matrix[i][j])
            dp = temp
        return min(dp)