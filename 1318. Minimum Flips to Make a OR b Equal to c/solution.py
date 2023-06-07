class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        binA = bin(a)[2:]
        binB = bin(b)[2:]
        binC = bin(c)[2:]
        maxN = max(len(binA), len(binB), len(binC))
        if len(binA) < maxN:
            binA = "0" * (maxN - len(binA)) + binA
        if len(binB) < maxN:
            binB = "0" * (maxN - len(binB)) + binB
        if len(binC) < maxN:
            binC = "0" * (maxN - len(binC)) + binC
        for i in range(maxN):
            a = binA[i]
            b = binB[i]
            c = binC[i]
            if (
                (a == "0" and b == "0" and c == "1")
                or (a == "1" and b == "0" and c == "0")
                or (a == "0" and b == "1" and c == "0")
            ):
                count += 1
            if a == "1" and b == "1" and c == "0":
                count += 2
        return count
