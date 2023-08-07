from bisect import bisect_left


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        r = bisect_left(
            matrix, target, key=lambda row: row[-1]
        )  # or key=itemgetter(-1)
        return r < len(matrix) and matrix[r][bisect_left(matrix[r], target)] == target
