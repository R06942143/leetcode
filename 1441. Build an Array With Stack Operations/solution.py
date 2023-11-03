class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        stream = 1
        ans = []
        for i in target:
            while i != stream:
                ans.extend(["Push", "Pop"])
                stream += 1
            ans.append("Push")
            stream += 1
        return ans