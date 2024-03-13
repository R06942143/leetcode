import math


class Solution:
    def pivotInteger2(self, n: int) -> int:
        sum_left = n*(n+1)/2
        sum_right = 0
        for i in range(n, 0, -1):
            if sum_right + i == sum_left:
                return i
            elif sum_right < sum_left:
                sum_right += i
                sum_left -= i
            else:
                return -1
        
        return -1
    
    def pivotInteger1(self, n: int) -> int:
        left = 1
        right = n
        sum_all = n*(n + 1)/2
        while left < right:
            mid = (left + right) //2
            left_sum = mid* (mid -1) / 2
            right_sum = sum_all - left_sum - mid
            if left_sum < right_sum:
                left = mid + 1
            else:
                right = mid
            
        return left if left*(left - 1)/2 == sum_all - left * (left + 1) /2 else -1

    def pivotInteger(self, n: int) -> int:
        total_sum = int(n * (n + 1) /2)
        x = int(math.sqrt(total_sum))
        return x if x*x == total_sum else -1
