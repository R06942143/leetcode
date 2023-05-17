class Solution:
    def reachableNodes(
        self, n: int, edges: list[list[int]], restricted: list[int]
    ) -> int:
        edge_map = {}
        for pair in edges:
            if pair[0] in edge_map:
                edge_map[pair[0]].append(pair[1])
            else:
                edge_map[pair[0]] = [pair[1]]
            if pair[1] in edge_map:
                edge_map[pair[1]].append(pair[0])
            else:
                edge_map[pair[1]] = [pair[0]]
        seen = {}
        restricted_map = {i: 1 for i in restricted}
        queue = [0]
        while queue:
            new_queue = []
            for i in queue:
                if i not in seen and i not in restricted_map:
                    new_queue.extend(edge_map[i])
                    seen[i] = 1
            queue = new_queue
        return len(seen)
