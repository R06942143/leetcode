class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        for c in s:
            if c == "1":
                ones += 1
        
        return (ones - 1) * "1" + (len(s) - ones) * "0" + "1"