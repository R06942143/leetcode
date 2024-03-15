class Solution:
    def productExceptSelf2(self, nums: list[int]) -> list[int]:
        prefix_product = [1] * len(nums)
        suffix_product = [1] * len(nums)
        prefix_product[0] = nums[0]
        suffix_product[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i]
            suffix_product[len(nums) - i - 1] = suffix_product[len(nums) - i] * nums[len(nums) - i - 1]
        
        ans = [0] * len(nums)
        for i in range(1, len(nums) - 1):
            ans[i] = prefix_product[i - 1] * suffix_product[i + 1]
        
        ans[0] = suffix_product[1]
        ans[-1] = prefix_product[-2]
        return ans

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)