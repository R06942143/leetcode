class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        highest = 0
        now = 0
        for height in gain:
            now += height
            if now > highest:
                highest = now
        return highest
