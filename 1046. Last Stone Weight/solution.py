import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            largest_stones = heapq.heappop(stones)
            second_stones = heapq.heappop(stones)
            new_stone = largest_stones - second_stones
            if new_stone:
                heapq.heappush(stones, new_stone)
        if stones:
            return -stones[0]
        return 0
