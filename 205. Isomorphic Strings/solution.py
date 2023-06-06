class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replaceMap = {}
        seen = {}
        for i in range(len(s)):
            if s[i] in replaceMap:
                if replaceMap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in seen:
                    return False
                seen[t[i]] = 1
                replaceMap[s[i]] = t[i]
        return True
