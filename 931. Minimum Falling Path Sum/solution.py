class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        for j in range(1, len(matrix)):
            for i in range(len(matrix[0])):
                if i == 0:
                    matrix[j][i] += min(matrix[j - 1][i], matrix[j - 1][i + 1])
                elif i == len(matrix[0]) - 1:
                    matrix[j][i] += min(matrix[j - 1][i - 1], matrix[j - 1][i])
                else:
                    matrix[j][i] += min(
                        matrix[j - 1][i - 1], matrix[j - 1][i], matrix[j - 1][i + 1]
                    )
        return min(matrix[-1])
