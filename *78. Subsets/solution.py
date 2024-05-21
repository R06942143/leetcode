class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.ans = []
        def helper(now, rest):
            if not rest:
                self.ans.append(now)
            else:
                helper(now + [rest[0]], rest[1:])
                helper(now, rest[1:])
        
        helper([], nums)

        return self.ans