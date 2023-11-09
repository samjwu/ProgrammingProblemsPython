class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 1e9+7
        
        ans = 0
        
        n = len(s)
        
        ptr1 = 0
        ptr2 = 0
        
        while ptr1 < n:
            while ptr2 < n and s[ptr1] == s[ptr2]:
                ptr2 += 1
                
            same = ptr2 - ptr1 + 1
            
            ans = (ans + self.kchoose2(same)) % mod
            
            ptr1 = ptr2
            
        return int(ans % mod)
    
    def kchoose2(self, k: int) -> int:
        return k * (k-1) // 2
