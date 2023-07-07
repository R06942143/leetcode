class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0
        r = 0
        now = {"T": 0, "F": 0}
        ans = 0
        while r < len(answerKey):
            now[answerKey[r]] += 1
            r += 1
            while min(now["T"], now["F"]) > k:
                now[answerKey[l]] -= 1
                l += 1
            ans = max(ans, r - l)
        return ans
