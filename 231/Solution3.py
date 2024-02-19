class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if n == 1:
            return True
        
        oneBits = 0
        
        for i in range(31):
            oneBits += n & 1
            n = n >> 1
            
        return oneBits == 1
