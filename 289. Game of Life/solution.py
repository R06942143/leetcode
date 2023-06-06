class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def liveOrDead(i: int, j: int) -> int:
            count = 0
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                    if (
                        i + ii > -1
                        and i + ii < len(self.tmp)
                        and j + jj > -1
                        and j + jj < len(self.tmp[0])
                    ):
                        print(i, j, i + ii, j + jj, self.tmp[i + ii][j + jj])
                        if self.tmp[i + ii][j + jj] == 1 and not (ii == 0 and jj == 0):
                            count += 1
            return count

        self.tmp = [[0] * len(board[0]) for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.tmp[i][j] = board[i][j]

        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors = liveOrDead(i, j)
                if board[i][j]:
                    if neighbors < 2:
                        board[i][j] = 0
                    elif neighbors < 4:
                        continue
                    else:
                        board[i][j] = 0
                else:
                    if neighbors == 3:
                        board[i][j] = 1
        del self.tmp
