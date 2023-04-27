from functools import lru_cache


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # greedy
        # O(n) O(1)
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0

        # O(n^2) O(n)
        # bottom up
        memoize = [0] * (len(nums))
        memoize[len(nums) - 1] = 1

        for i in range(len(nums) - 2, -1, -1):
            maxJump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, maxJump + 1):
                if memoize[j] == 1:
                    memoize[i] = 1
                    break
        return memoize[0] == 1

        # O(n^2) O(n)
        # top down with dp
        if not nums:
            return False

        @lru_cache(None)
        def recursion(n):
            if n >= len(nums) - 1:
                return True

            for i in range(1, nums[n] + 1):
                if recursion(n + i):
                    return True
            return False

        return recursion(0)
