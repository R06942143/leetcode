class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dump = float("inf")
        for j in range(1, len(triangle)):
            triangle[j - 1] = [dump] + triangle[j - 1]
            for i in range(len(triangle[j])):
                triangle[j][i] += min(triangle[j - 1][i : i + 2])
        return min(triangle[-1])
