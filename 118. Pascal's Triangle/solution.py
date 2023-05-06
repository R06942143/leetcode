class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        self.ans = [[1]]
        for n in range(1, numRows):
            temp = [1] * (n + 1)
            if n > 1:
                for i in range(1, n):
                    temp[i] = self.ans[-1][i - 1] + self.ans[-1][i]
            self.ans.append(temp)
        return self.ans
