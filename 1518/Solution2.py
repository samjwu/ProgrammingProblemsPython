class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        
        empties = 0
        
        while numBottles > 0:
            ans += numBottles
            empties += numBottles
            
            numBottles = empties // numExchange
            empties %= numExchange
            
        return ans
