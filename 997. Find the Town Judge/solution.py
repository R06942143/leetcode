class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        indegree_map = {i : [] for i in range(1, n+1)}
        outdegree_map = {i: [] for i in range(1, n+1)}

        for relationship in trust:
            indegree_map[relationship[1]].append(relationship[0])
            outdegree_map[relationship[0]].append(relationship[1])
        
        condition_one = set()
        for key, value in outdegree_map.items():
            if value == []:
                condition_one.add(key)
        
        condition_two = set()
        for key, value in indegree_map.items():
            if len(value) == n - 1:
                condition_two.add(key)

        ans = condition_one.intersection(condition_two)
        if len(ans) == 1:

            return ans.pop()
        
        return -1

    def better_answer(self, n: int, trust: list[list[int]]) -> int:
        count = [0] * (n + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, n + 1):
            if count[i] == n - 1:
                return i
        return -1