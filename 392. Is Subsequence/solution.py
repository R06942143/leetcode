class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        now = s[0]
        s = s[1:]
        for c in t:
            if c == now:
                if s == "":
                    return True
                else:
                    now = s[0]
                    s = s[1:]
        return False
