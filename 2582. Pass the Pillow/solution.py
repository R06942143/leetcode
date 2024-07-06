class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        direction = False

        while time > 0:
            if not direction:
                i += 1
            else:
                i -= 1
            time -= 1
            if i == n:
                direction = True
            if i == 1:
                direction = False
        return i
