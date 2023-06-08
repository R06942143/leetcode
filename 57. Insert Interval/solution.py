class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()
        now = 0
        while now < len(intervals) - 1:
            one = intervals[now]
            two = intervals[now + 1]
            if one[1] >= two[0]:
                one[1] = max(two[1], one[1])
                intervals.remove(two)
            else:
                now += 1
        return intervals
