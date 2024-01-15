from collections import defaultdict


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        lose_map = defaultdict(int)
        all_player = set()

        for ppl in matches:
            lose_map[ppl[1]] += 1
            all_player.add(ppl[0])
            all_player.add(ppl[1])
        ans = [[], []]
        for player in sorted(all_player):
            if lose_map[player] == 0:
                ans[0].append(player)
            if lose_map[player] == 1:
                ans[1].append(player)
        
        return ans
