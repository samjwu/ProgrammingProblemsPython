class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        
        if n == 2:
            return 1
        
        ans = [0 for i in range(n+1)]
        ans[1] = 1
        ans[2] = 1
        
        for i in range(3, n+1):
            ans[i] = ans[i-3] + ans[i-2] + ans[i-1]
            
        return ans[n]
