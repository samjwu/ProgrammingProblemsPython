class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        
        prefix = [0]
        for num in arr:
            prefix.append(num)
            
        for idx in range(1, n+1):
            prefix[idx] ^= prefix[idx-1]
        
        ans = 0
        
        for l in range(n+1):
            for r in range(l+1, n+1):
                if prefix[l] == prefix[r]:
                    ans += r-l-1
                    
        return ans
