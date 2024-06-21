class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        total_s = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total_s += customers[i]
        
        ans = 0

        for i in range(minutes):
            if i < len(customers):
                total_s += customers[i] * grumpy[i]
        
        ans = total_s

        for i in range(len(customers)):
            if i + minutes < len(customers):
                total_s -= customers[i] * grumpy[i]
                total_s += customers[i + minutes] * grumpy[i + minutes]
                ans = max(ans, total_s)

        return ans
        
