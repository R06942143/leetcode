class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for num in range(1, n**2 + 1):
            A[i][j] = num
            if A[(i + di) % n][(j + dj) % n] != 0:
                di, dj = dj, -di
            i += di
            j += dj
        return A
