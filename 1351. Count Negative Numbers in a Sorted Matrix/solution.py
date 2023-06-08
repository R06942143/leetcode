from bisect import bisect_left


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        for g_list in grid:
            pos = bisect_left(g_list[::-1], 0)
            count += pos
        return count
