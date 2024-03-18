class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()

        i = 0
        while i < len(points) - 1:
            if points[i][1] >= points[i + 1][0]:
                points[i] = [points[i + 1][0], min(points[i][1], points[i + 1][1])]
                points.remove(points[i + 1])
            else:
                i += 1

        return len(points)
    
    def betterFindMinArrowShots(self, points: list[list[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        arrow = 1
        end = points[0][1]
        for point in points:
            if point[0] > end:
                end = point[1]
                arrow += 1
        return arrow