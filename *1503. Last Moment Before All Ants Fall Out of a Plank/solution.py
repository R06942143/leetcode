class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        ans = 0
        for num in left:
            ans = max(ans, num)
        
        for num in right:
            ans = max(ans, n - num)
        
        return ans