from copy import deepcopy


class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.mat = matrix
        self.row = len(matrix)
        self.column = len(matrix[0])
        self._init_matrix(self.mat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        all_sum = self.dp[row2][col2]
        if col1 - 1 >= 0:
            all_sum -= self.dp[row2][col1 - 1]
        if row1 - 1 >= 0:
            all_sum -= self.dp[row1 - 1][col2]
        if col1 - 1 >= 0 and row1 - 1 >= 0:
            all_sum += self.dp[row1 - 1][col1 - 1]
        return all_sum

    def _init_matrix(self, matrix: list[list[int]]):
        dp = deepcopy(self.mat)
        for i in range(len(self.mat)):
            for j in range(1, len(self.mat[0])):
                dp[i][j] += dp[i][j - 1]
        for i in range(1, len(self.mat)):
            for j in range(len(self.mat[0])):
                dp[i][j] += dp[i - 1][j]
        self.dp = dp


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
