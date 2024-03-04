class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        score = 0
        low = 0
        height = len(tokens) - 1

        while low <= height:
            if power >= tokens[low]:
                score += 1
                power -= tokens[low]
                low += 1
            elif score != 0 and low < height:
                score -= 1
                power += tokens[height]
                height -= 1
            else:
                return score
        
        return score