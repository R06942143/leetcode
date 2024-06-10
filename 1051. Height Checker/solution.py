class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        order_heights = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i] != order_heights[i]:
                ans += 1
        
        return ans