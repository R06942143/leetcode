from math import comb


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ans = [0] * (rowIndex + 1)
        
        for i in range(rowIndex + 1):
            ans[i] = comb(rowIndex, i) # nCr = n! / (r! * (n - r)!) n choose r
        
        return ans