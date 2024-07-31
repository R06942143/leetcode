import sys

class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [sys.maxsize] * n
        dp[0] = books[0][1]                                # first book will always on it's own row
        for i in range(1, n):                              # for each book
            cur_w, height_max = books[i][0], books[i][1]
            dp[i] = dp[i-1] + height_max                   # initialize result for current book `dp[i]`
            for j in range(i-1, -1, -1):                   # for each previou `book[j]`, verify if it can be placed in the same row as `book[i]`
                if cur_w + books[j][0] > shelfWidth: break
                cur_w += books[j][0]
                height_max = max(height_max, books[j][1])  # update current max height
                dp[i] = min(dp[i], (dp[j-1] + height_max) if j-1 >= 0 else height_max) # always take the maximum heigh on current row
        return dp[n-1]