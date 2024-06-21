class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        if minutes >= n:
            return sum(customers)
        
        ans = 0
        
        baseAns = 0
        
        for i in range(n):
            baseAns += (1 - grumpy[i]) * customers[i]
        
        l = 0
        r = 0
        
        while r < n:
            baseAns += grumpy[r] * customers[r]
            r += 1
            
            if r - l == minutes:
                ans = max(ans, baseAns)
                baseAns -= grumpy[l] * customers[l]
                l += 1
            
        return ans
