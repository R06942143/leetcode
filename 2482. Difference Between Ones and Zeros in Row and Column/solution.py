class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        diff_row = [0] * len(grid)
        diff_col = [0] * len(grid[0])
        for i in range(len(diff_row)):
            tmp = 0
            for num in grid[i]:
                if num == 1:
                    tmp +=1
                else:
                    tmp -= 1
            diff_row[i] = tmp
        
        for i in range(len(diff_col)):
            tmp = 0
            for j in range(len(diff_row)):
                if grid[j][i] == 1:
                    tmp += 1
                else:
                    tmp -= 1
            diff_col[i] = tmp
        diff = [[0] * len(grid[0]) for _ in range(len(grid)) ]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j] = diff_row[i] + diff_col[j]
        
        return diff