class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if n == 1:
            return True
        
        return (1 << 31) % n == 0
