class Solution:
    def pivotInteger(self, n: int) -> int:
        sum1 = 0
        
        sum2 = 0
        
        for i in range(1, n+1):
            sum2 += i
            
        for i in range(1, n+1):
            sum1 += i
            
            if sum1 == sum2:
                return i
            
            sum2 -= i
            
        return -1
