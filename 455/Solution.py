class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        m = len(g)
        n = len(s)
        
        ans = 0
        cookie = 0
        
        while ans < m and cookie < n:
            if s[cookie] >= g[ans]:
                ans += 1
                
            cookie += 1
            
        return ans
