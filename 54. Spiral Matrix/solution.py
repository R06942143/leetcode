class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        while matrix:
            ans.extend(matrix[0])
            del matrix[0]
            matrix = list(zip(*matrix))[::-1]
        return ans
