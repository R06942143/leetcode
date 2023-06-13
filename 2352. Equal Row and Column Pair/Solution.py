class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        ans =0
        pairMap = defaultdict(int)
        reverse_grid = list(zip(*grid))
        for i in range(len(grid)):
            pairMap[reverse_grid[i]] += 1
        for i in range(len(grid)):
            if tuple(grid[i]) in pairMap:
                ans += pairMap[tuple(grid[i])]
        return ans
