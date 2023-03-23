# 1319. Number of Operations to Make Network Connected
## DFS
If the number of cables is less than the computer - 1, we return -1

And the final answer is the group of computers -1.

### Time Complexity
O(V+E), where V is the number of vertices and E is the number of edges in the graph.

### SPACE Complexity
Space complexity:
The space complexity of the DFS algorithm is O(V).
And we are making adjacency list is O(V+E)