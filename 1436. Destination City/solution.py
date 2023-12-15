from collections import defaultdict


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        destCityMap = defaultdict(str)
        for path in paths:
            destCityMap[path[0]] = path[1]

        for _, value in destCityMap.items():
            if value not in destCityMap:
                return value
        return ""