class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        self.mat = mat
        dp = [[0] * len(mat[0]) for _ in range(len(mat))]

        def matrixSum(k: int, i: int, j: int) -> int:
            ans = 0
            for ii in range(max(0, i - k), min(len(mat), i + k + 1)):
                for jj in range(max(0, j - k), min(len(mat[0]), j + k + 1)):
                    ans += self.mat[ii][jj]
            return ans

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dp[i][j] = matrixSum(k, i, j)
        return dp
