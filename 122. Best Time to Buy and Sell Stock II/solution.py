class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        prev_px = float("inf")
        profit = 0

        for px in prices:
            if px > prev_px:
                profit += px - prev_px

            prev_px = px

        return profit
