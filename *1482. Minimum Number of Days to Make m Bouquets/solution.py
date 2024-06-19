class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)
        l = min(bloomDay)
        h = max(bloomDay)
        if m*k > len(bloomDay):
            return -1
        while l <= h:
            mid = (l+h)//2
            check = False
            c = 0
            noOfb = 0
            for b in bloomDay:
                if b <= mid:
                    c += 1
                else:
                    noOfb += c//k
                    c = 0
            noOfb += c//k
            if noOfb>=m:
                check = True
            if check:
                h = mid - 1
            else:
                l = mid + 1
        return l 
        