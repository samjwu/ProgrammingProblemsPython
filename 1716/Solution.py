class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        
        curr = 0
        mon = 0
        
        for i in range(n):
            if i % 7 == 0:
                mon += 1
                curr = mon
            else:
                curr += 1
            
            ans += curr
            
        return ans
