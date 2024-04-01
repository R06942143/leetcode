class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        have_word = False
        ans = 0

        for i in range(len(s)):
            now = s[len(s) -i -1]
            if not have_word and now == ' ':
                continue
            elif now == ' ':
                return ans
            else:
                ans += 1
                have_word = True

        return ans 