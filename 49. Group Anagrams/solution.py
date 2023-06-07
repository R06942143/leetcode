from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        wordMap = defaultdict(list)
        for word in strs:
            s = "".join(sorted(word))
            wordMap[s].append(word)
        return wordMap.values()
