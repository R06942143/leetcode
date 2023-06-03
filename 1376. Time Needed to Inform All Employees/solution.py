class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: list[int], informTime: list[int]
    ) -> int:
        subordinates = {}
        for i in range(len(manager)):
            if manager[i] in subordinates:
                subordinates[manager[i]].append(i)
            else:
                subordinates[manager[i]] = [i]

        def dfs(employee: int, time: int):
            maxTime = 0
            if employee not in subordinates or subordinates[employee] == []:
                return time
            for subordinate in subordinates[employee]:
                maxTime = max(maxTime, dfs(subordinate, time + informTime[employee]))
            return maxTime

        return dfs(headID, 0)
