class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j]) and i != 0 and j != 0:
                    matrix[i][j] = (
                        min(
                            int(matrix[i - 1][j]),
                            int(matrix[i][j - 1]),
                            int(matrix[i - 1][j - 1]),
                        )
                        + 1
                    )
                if int(matrix[i][j]) > ans:
                    ans = int(matrix[i][j])
        return ans**2
