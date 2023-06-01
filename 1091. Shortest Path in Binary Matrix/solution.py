class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        queue = []
        if grid[0][0] == 0:
            queue.append((0, 0))
        count = 1

        while queue:
            new_queue = []
            for position in queue:
                dx = position[0]
                dy = position[1]
                if position == (len(grid) - 1, len(grid) - 1):
                    return count
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (
                            0 <= dx + i < len(grid)
                            and 0 <= dy + j < len(grid)
                            and grid[dx + i][dy + j] == 0
                        ):
                            new_queue.append((dx + i, dy + j))
                            grid[dx + i][dy + j] = 1
            queue = new_queue
            count += 1
        return -1
