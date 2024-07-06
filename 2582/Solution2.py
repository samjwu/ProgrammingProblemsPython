class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # each time pillow reaches an end is a pass
        passes = time // (n-1)
        
        remainder = time % (n-1)
        
        # even passes means direction is positive
        # odd passes means direction is negative
        if passes % 2 == 0:
            return 1 + remainder
        
        return n - remainder
