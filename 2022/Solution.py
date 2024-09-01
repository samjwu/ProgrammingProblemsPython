class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        
        ans = [[0 for j in range(n)] for i in range(m)]
        
        for idx in range(m*n):
            i = idx // n
            j = idx % n
            ans[i][j] = original[idx]

        return ans
