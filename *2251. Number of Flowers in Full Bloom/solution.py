from bisect import bisect_left, bisect_right


class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        start = sorted([s for s, e in flowers])
        end = sorted([e for s, e in flowers])
        return [bisect_right(start, t) - bisect_left(end, t) for t in people]