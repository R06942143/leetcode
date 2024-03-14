import collections


class Solution:
    def numSubarraysWithSum(self, A, S):
        c = collections.Counter({0: 1})
        psum = res = 0
        for i in A:
            psum += i
            res += c[psum - S]
            c[psum] += 1
        return res

    def tle_answer(self, nums: list[int], goal: int) -> int:
        ans = 0
        for left in range(len(nums)):
            now = 0
            for right in range(left, len(nums)):
                now += nums[right]
                if now == goal:
                    ans += 1
        
        return ans