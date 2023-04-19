# DFS vs BFS
1. If you know a solution is not far from the root of the tree, a breadth first search (BFS) might be better.

2. If the tree is very deep and solutions are rare, depth first search (DFS) might take an extremely long time, but BFS could be faster.

3. If the tree is very wide, a BFS might need too much memory, so it might be completely impractical.

4. If solutions are frequent but located deep in the tree, BFS could be impractical.

5. If the search tree is very deep you will need to restrict the search depth for depth first search (DFS), anyway (for example with iterative deepening).

But these are just rules of thumb; you'll probably need to experiment.