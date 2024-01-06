from bisect import bisect_right


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        ind = 0
        for e, s, p in sorted(zip(endTime, startTime, profit)):
            startTime[ind] = s
            endTime[ind]   = e
            profit[ind]    = p
            ind += 1
        
        for i in range(1, len(profit)):

            index = bisect_right(endTime, startTime[i]) - 1
            profit[i] = max(profit[i - 1], (profit[index] if index >= 0 else 0) + profit[i])

        return profit[-1]
