class Solution:
    def minOperations(self, s: str) -> int:
        start_from_one = 1
        start_from_zero = 0
        count_one = 0
        count_zero = 0
        for i in s:
            if int(i) != start_from_zero:
                count_zero += 1
            if int(i) != start_from_one:
                count_one += 1
            
            start_from_zero = not start_from_zero
            start_from_one = not start_from_one
        return min(count_one, count_zero)

    def minOperations_good(self, s: str) -> int:
        startsWith0 = 0
        flag = 0 # here we are first calculating the soln starting with 0, so flag = 0

        for c in s:
            if int(c) != flag:
                startsWith0 += 1

            flag = not flag # alternates b/w 0 & 1

        startsWith1 = len(s) - startsWith0
        return min(startsWith0, startsWith1)