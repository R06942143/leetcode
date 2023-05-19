class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = 1
        color_map = {0: color}

        queue = [0]
        while queue:
            color *= -1
            new_queue = []
            for node in queue:
                for neighbor in graph[node]:
                    if neighbor not in color_map:
                        new_queue.append(neighbor)
                        color_map[neighbor] = color
                    else:
                        if color_map[node] == color_map[neighbor]:
                            return False
            queue = []
            if new_queue:
                queue = new_queue
            elif len(color_map) != len(graph):
                for i in range(len(graph)):
                    if i not in color_map and not queue:
                        queue = [i]
                        color_map[i] = color

        return True
