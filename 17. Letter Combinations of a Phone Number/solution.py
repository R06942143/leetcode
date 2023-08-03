class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapping = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": " ",
        }
        newlist = []
        if len(digits) == 0:
            return ""
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        for i in prev:
            for j in list(mapping[digits[-1]]):
                newlist.append(i + j)
        return newlist
