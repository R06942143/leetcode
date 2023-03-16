class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ## sort each row
        ## O(m*(nlogn))
        for m in range(len(grid)):
            grid[m] = sorted(grid[m])

        answer = 0
        ## O(m*n)
        for n in range(len(grid[0])):
            max_number = 0
            for m in range(len(grid)):
                value = grid[m][n]
                if value > max_number:
                    max_number = value
            answer += max_number
        return answer