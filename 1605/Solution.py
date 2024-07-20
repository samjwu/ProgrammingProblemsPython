class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        
        currRow = [0 for i in range(m)]
        currCol = [0 for j in range(n)]
        
        ans = [[0 for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                ans[i][j] = min(rowSum[i] - currRow[i], colSum[j] - currCol[j])
                
                currRow[i] += ans[i][j]
                currCol[j] += ans[i][j]
                
        return ans
