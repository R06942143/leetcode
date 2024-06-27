from collections import defaultdict


class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        edge_map = defaultdict(list)

        for i in edges:
            edge_map[i[0]].append(i[1])
            edge_map[i[1]].append(i[0])
        
        for key, value in edge_map.items():
            if len(value) == len(edges):
                return key
        
        return -1