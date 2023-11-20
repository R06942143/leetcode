class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        minutes = 0
        last_M = 0
        last_P = 0
        last_G = 0
        for i in range(len(garbage)):
            if "M" in garbage[len(garbage) - 1 - i] and last_M == 0:
                last_M = len(garbage) - 1 - i
            if "P" in garbage[len(garbage) - 1 - i] and last_P == 0:
                last_P = len(garbage) - 1 - i
            if "G" in garbage[len(garbage) - 1 - i] and last_G == 0:
                last_G = len(garbage) - 1 - i
           
        for i in range(len(garbage)):
            if i <= last_M:
                minutes += garbage[i].count('M')
                if i != 0:
                    minutes += travel[i - 1]
            if i <= last_P:
                minutes += garbage[i].count('P')
                if i != 0:
                    minutes += travel[i - 1]
            if i <= last_G:
                minutes += garbage[i].count('G')
                if i != 0:
                    minutes += travel[i - 1]

        return minutes