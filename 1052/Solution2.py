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
        
        l = 0
        r = 0
        
        while r < n:
            if grumpy[r] == 1:
                baseAns += customers[r]
            r += 1
            
            if r - l == minutes:
                ans = max(ans, baseAns)
                if grumpy[l] == 1:
                    baseAns -= customers[l]
                l += 1
            
        return ans
