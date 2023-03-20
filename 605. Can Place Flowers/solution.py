class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        ## padding a zero to determine if we could place in the first place
        zeros, ans = 1, 0  
        for f in flowerbed:
            if f == 0: 
                zeros += 1
            else:
                ans += (zeros - 1) // 2
                zeros = 0
        ## add the remain zeros
        return ans + zeros // 2 >= n 