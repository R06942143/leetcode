from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        modulo = 10 ** 9 + 7

        @lru_cache(None)
        def recursion(move, row, col):
            if row == m or row < 0 or col == n or col < 0:
                return 1
            if move == 0:
                return 0
            move -= 1
            return (
                recursion(move, row, col + 1)
                + recursion(move, row, col - 1)
                + recursion(move, row - 1, col)
                + recursion(move, row + 1, col)
            ) % modulo
        return recursion(maxMove, startRow, startColumn)