class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if t == 1 and sx == fx and sy == fy:
            return False
        if fx - sx > 0:
            dx = fx - sx
        else:
            dx = sx - fx
        if fy - sy > 0:
            dy = fy - sy
        else:
            dy = sy - fy
        
        return max(dx, dy) <= t