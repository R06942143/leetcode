from collections import deque
import heapq


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        costs_deque = deque(costs)
        rhp = []
        lhp = []
        i = 0
        ans = 0
        while i < k:
            while len(lhp) < candidates and costs_deque:
                heapq.heappush(lhp, costs_deque.popleft())
            while len(rhp) < candidates and costs_deque:
                heapq.heappush(rhp, costs_deque.pop())
            if not rhp:
                ans += heapq.heappop(lhp)
            elif not lhp:
                ans += heapq.heappop(rhp)
            elif lhp[0] <= rhp[0]:
                ans += heapq.heappop(lhp)
            else:
                ans += heapq.heappop(rhp)
            i += 1

        return ans
