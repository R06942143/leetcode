class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        now = 0
        while now < len(points) - 1:
            one = points[now]
            two = points[now + 1]
            if one[1] >= two[0]:
                one[0] = max(one[0], two[0])
                one[1] = min(one[1], two[1])
                points.remove(two)
            else:
                now += 1
        return len(points)
