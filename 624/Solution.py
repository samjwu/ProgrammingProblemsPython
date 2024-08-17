class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)
        
        lo = arrays[0][0]
        hi = arrays[0][-1]
        
        ans = 0
        
        for i in range(1, m):
            ans = max(ans, hi - arrays[i][0], arrays[i][-1] - lo)
            lo = min(lo, arrays[i][0])
            hi = max(hi, arrays[i][-1])
            
        return ans
