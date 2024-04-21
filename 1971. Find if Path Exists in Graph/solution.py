from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph_map = defaultdict(set)

        for edge in edges:
            graph_map[edge[0]].add(edge[1])
            graph_map[edge[1]].add(edge[0])
        
        seen = set([source])
        queue = [source]
        while queue:
            next_queue = []
            for node in queue:
                if node == destination:
                    return True

                next_queue.extend(list(graph_map[node].difference(seen)))
                seen = seen.union(graph_map[node])

            queue = next_queue

        return False