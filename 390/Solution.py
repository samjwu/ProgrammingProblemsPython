class Solution:
    def lastRemaining(self, n: int) -> int:
        remaining = n
        left = True
        step_size = 1
        curr = 1
        
        while remaining > 1:
            if left or remaining % 2 == 1:
                curr += step_size
            
            remaining //= 2
            
            step_size *= 2
            
            left = not left
        
        return curr
