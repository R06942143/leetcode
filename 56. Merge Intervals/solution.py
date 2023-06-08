class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) < 2:
            return intervals
        now = 0
        intervals.sort(key=lambda x: x[0])
        while now < len(intervals) - 1:
            this = intervals[now]
            next_one = intervals[now + 1]
            if this[1] >= next_one[0]:
                this[1] = max(next_one[1], this[1])
                intervals.remove(next_one)
            else:
                now += 1
        return intervals
