from collections import defaultdict, deque


class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        adjacentMap = defaultdict(list)
        for i in adjacentPairs:
            adjacentMap[i[0]].append(i[1])
            adjacentMap[i[1]].append(i[0])

        seen = {adjacentPairs[0][0], adjacentPairs[0][1]}
        ans = deque([adjacentPairs[0][0], adjacentPairs[0][1]])
        ## find left
        while adjacentMap[ans[0]][0] not in seen or adjacentMap[ans[0]][-1] not in seen:
            now = ans[0]
            if adjacentMap[now][0] not in seen:
                ans.appendleft(adjacentMap[now][0])
                seen.add(adjacentMap[now][0])
            elif adjacentMap[now][-1] not in seen:
                ans.appendleft(adjacentMap[now][-1])
                seen.add(adjacentMap[now][-1])
        ## find right
        while adjacentMap[ans[-1]][0] not in seen or adjacentMap[ans[-1]][-1] not in seen:
            now = ans[-1]
            if adjacentMap[now][0] not in seen:
                ans.append(adjacentMap[now][0])
                seen.add(adjacentMap[now][0])
            elif adjacentMap[now][-1] not in seen:
                ans.append(adjacentMap[now][-1])
                seen.add(adjacentMap[now][-1])


        return ans