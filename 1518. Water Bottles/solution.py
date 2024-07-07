class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        numFull = numBottles
        numEmpty = 0

        while numFull:
            ans += numFull
            x = numFull + numEmpty
            numFull = (x) // numExchange
            numEmpty = (x) % numExchange
        
        return ans