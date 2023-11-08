class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(fx - sx)
        dy = abs(fy - sy)
        
        time = max(dx, dy)
        
        # edge case since we MUST move
        if dx == 0 and dy == 0 and t == 1:
            return False
        
        return t >= time
