class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        
        if k == n:
            return "0"
        
        stk = []
        
        idx = 0
        
        while idx < n:
            m = len(stk)
            
            while k > 0 and m > 0 and stk[m-1] > num[idx]:
                stk.pop()
                k -= 1
                m -= 1
        
            stk.append(num[idx])
            idx += 1
            
        while k > 0:
            stk.pop()
            k -= 1
            
        m = len(stk)
        
        ans = ""
        
        while m > 0:
            ans = str(stk[m-1]) + ans
            stk.pop()
            m -= 1
        
        ans = ans.lstrip("0")
        
        if len(ans) == 0:
            return "0"
        return ans
