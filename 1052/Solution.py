class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        if minutes >= n:
            return sum(customers)
        
        ans = 0
        
        baseAns = 0
        
        for i in range(n):
            if grumpy[i] == 0:
                baseAns += customers[i]
                
        for i in range(n-minutes+1):
            subAns = baseAns
            
            for j in range(minutes):
                if grumpy[i+j] == 1:
                    subAns += customers[i+j]
                    
            ans = max(ans, subAns)
        
        return ans
