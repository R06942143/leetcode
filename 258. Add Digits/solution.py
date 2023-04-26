class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            new = 0
            for i in str(num):
                new += int(i)
            num = new
        return num
