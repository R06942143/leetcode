import math


class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        arrived = [ math.ceil(dist[i]/speed[i]) for i in range(len(dist))]
        arrived.sort()
        now = 0
        for monster in arrived:
            if monster > now:
                now += 1
            else:
                return now

        return now