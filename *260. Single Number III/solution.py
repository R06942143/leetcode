class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor_result = 0

        # XOR all numbers to find the XOR of the two distinct numbers
        for num in nums:
            xor_result ^= num

        # Find the rightmost set bit
        mask = xor_result & -xor_result

        num1, num2 = 0, 0

        # Separate the numbers based on the rightmost set bit
        for num in nums:
            if (num & mask) != 0:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]