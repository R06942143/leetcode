class Solution:
    def sequentialDigits(self, low, high):
        
        lower , higher = len(list(str(low))) , len(list(str(high)))
        string = "123456789"
        res = []
        for i in range(lower, higher + 1):
            for j in range(10 - i):
                temp = int(string[j:j+i])
                if low <= temp <= high:
                    res.append(temp)
        return res
    