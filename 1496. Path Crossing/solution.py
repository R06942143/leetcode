from collections import defaultdict


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visit = defaultdict(tuple)
        x = 0
        y = 0
        visit[(0, 0)] = True
        for i in path:
            if i == 'N':
                y += 1
            if i == 'S':
                y -= 1
            if i == 'E':
                x += 1
            if i == 'W':
                x -= 1
            
            if visit[(x, y)] == True:
                return True
            
            visit[(x, y)] = True
        
        return False