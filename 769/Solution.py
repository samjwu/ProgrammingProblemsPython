class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        
        hi = 0
        
        ans = 0
        
        for i in range(n):
            hi = max(hi, arr[i])
            
            if i == hi:
                ans += 1
        
        return ans
