class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        for u, v in roads:
            degrees[u] += 1
            degrees[v] += 1

        sorted_degrees = sorted(set(degrees), reverse=True)
        max_deg = sorted_degrees[0]
        second_max_deg = sorted_degrees[1] if len(sorted_degrees) > 1 else 0

        max_count = degrees.count(max_deg)
        second_max_count = degrees.count(second_max_deg)

        if max_count > 1:
            directly_connected = sum(1 for u, v in roads if degrees[u] == max_deg and degrees[v] == max_deg)
            possible_connections = max_count * (max_count - 1) // 2
            return 2 * max_deg - 1 if possible_connections == directly_connected else 2 * max_deg

        direct_connections_to_second = sum(1 for u, v in roads if (degrees[u], degrees[v]) in [(max_deg, second_max_deg), (second_max_deg, max_deg)])
        return max_deg + second_max_deg - 1 if second_max_count == direct_connections_to_second else max_deg + second_max_deg
