import math


class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        def can_reach(speed):
            so_far = 0
            for i in range(len(dist) - 1):
                so_far += math.ceil(dist[i] / speed)
                if so_far > hour:
                    return False
            return (so_far + (dist[-1] / speed)) <= hour

        l = 1
        r = 10**7
        max_speed = -1
        while l <= r:
            m = (l + r) // 2
            if can_reach(m):
                max_speed = m
                r = m - 1
            else:
                l = m + 1
        return max_speed
