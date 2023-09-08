class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        import math

        triangle = []
        
        for n in range(numRows):
            row = []
            for k in range(n+1):
                row.append(math.comb(n, k))
            triangle.append(row)
        
        return triangle