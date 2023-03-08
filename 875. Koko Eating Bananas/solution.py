import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        right = max(piles)
        left = midSpeed = 1
        while left < right:
            print(left, right)
            midSpeed = (right + left) // 2
            totalHour = self.countSpeed(piles, midSpeed)
            
            if totalHour <= h:
                right = midSpeed
            else:
                left = midSpeed + 1
        return right

    def countSpeed(self, piles: list[int], speed: int) -> int:
        total = 0
        for bananas in piles:
            total += math.ceil(bananas/speed)
        return total