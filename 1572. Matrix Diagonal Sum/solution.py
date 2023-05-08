class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j:
                    ans += mat[i][j]
                elif i + j == len(mat) - 1:
                    ans += mat[i][j]
        return ans
