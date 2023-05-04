from collections import defaultdict


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        position = 0
        all_senator = defaultdict(int)
        for senator in senate:
            all_senator[senator] += 1
        ban = defaultdict(int)
        while senate:
            if not all_senator["R"]:
                return "Dire"
            if not all_senator["D"]:
                return "Radiant"
            if senate[position] == "R":
                if ban["R"] != 0:
                    senate = senate[:position] + senate[position + 1 :]
                    ban["R"] -= 1
                    all_senator["R"] -= 1
                else:
                    ban["D"] += 1
                    position += 1
            else:
                if ban["D"] != 0:
                    senate = senate[:position] + senate[position + 1 :]
                    ban["D"] -= 1
                    all_senator["D"] -= 1
                else:
                    ban["R"] += 1
                    position += 1
            position = position % len(senate)
