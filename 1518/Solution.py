class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        
        empties = 0
        
        while numBottles > 0:
            ans += numBottles
            empties += numBottles
            
            newBottles = empties // numExchange
            empties %= numExchange
            
            numBottles = newBottles
            
        return ans
