class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        steps = 0
        now = points[0]
        for i in range(1, len(points)):
            steps += max(abs(points[i][0] - now[0]), abs(points[i][1] - now[1]))
            now = points[i]
        
        return steps