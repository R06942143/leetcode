class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        root_island = self.findFirst(grid)
        self.bfs = {root_island: 1}
        queue = [root_island]
        while queue:
            new_queue = []
            for node in queue:
                for x, y in [
                    (node[0] - 1, node[1]),
                    (node[0] + 1, node[1]),
                    (node[0], node[1] - 1),
                    (node[0], node[1] + 1),
                ]:
                    if (
                        0 <= x < len(grid)
                        and 0 <= y < len(grid[0])
                        and grid[x][y] == 1
                        and (x, y) not in self.bfs
                    ):
                        self.bfs[(x, y)] = 1
                        new_queue.append((x, y))
            queue = new_queue

        queue = list(self.bfs)
        count = -1
        while queue:
            count += 1
            new_queue = []
            for node in queue:
                for x, y in [
                    (node[0] - 1, node[1]),
                    (node[0] + 1, node[1]),
                    (node[0], node[1] - 1),
                    (node[0], node[1] + 1),
                ]:
                    if (
                        0 <= x < len(grid)
                        and 0 <= y < len(grid[0])
                        and (x, y) not in self.bfs
                    ):
                        if grid[x][y] == 1:
                            return count
                        else:
                            self.bfs[(x, y)] = 1
                            new_queue.append((x, y))
            queue = new_queue

    def findFirst(self, grid: List[List[int]]) -> list[int]:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return (i, j)
        return (-1, -1)
