import heapq

class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.adj_list = {i: [] for i in range(n)}
        for edge in edges:
            self.adj_list[edge[0]].append((edge[1], edge[2]))
        
    def addEdge(self, edge: list[int]) -> None:
        self.adj_list[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        dist = {i: float('inf') for i in range(len(self.adj_list))}
        dist[node1] = 0
        
        while heap:
            (d, node) = heapq.heappop(heap)
            if node == node2:
                return d
            if d > dist[node]:
                continue
            for neighbor, weight in self.adj_list[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
                    
        return -1