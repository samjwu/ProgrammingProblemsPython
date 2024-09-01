class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        
        ans = [[0 for j in range(n)] for i in range(m)]
        
        idx = 0
        
        for i in range(m):
            for j in range(n):
                ans[i][j] = original[idx]
                idx += 1
                
        return ans
