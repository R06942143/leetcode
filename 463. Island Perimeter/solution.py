class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i -1 < 0:
                        ans += 1
                    elif grid[i-1][j] == 0:
                        ans += 1
                    if  i+1 > len(grid) -1:
                        ans += 1
                    elif grid[i+1][j] == 0:
                        ans += 1
                    
                    if j -1 < 0:
                        ans += 1
                    elif grid[i][j-1] == 0:
                        ans += 1
                    if j+1 > len(grid[0]) -1:
                        ans += 1
                    elif grid[i][j+1] == 0:
                        ans += 1
        return ans
                
                
                               

                