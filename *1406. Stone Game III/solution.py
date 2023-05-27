class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        seen = {}

        def maxWin(idx):
            if idx == len(stoneValue):
                return 0
            if idx in seen:
                return seen[idx]

            myStone = 0
            res = float("-inf")
            for i in range(idx, min(idx + 3, len(stoneValue))):
                myStone += stoneValue[i]
                res = max(res, myStone - maxWin(i + 1))
            seen[idx] = res
            return res

        res = maxWin(0)
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        else:
            return "Tie"
