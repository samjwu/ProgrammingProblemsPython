class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        ans = [[-1 for j in range(n-2)] for i in range(n-2)]
        
        for i in range(n-2):
            for j in range(n-2):
                row = i+1
                col = j+1
                
                hi = -1
                
                for k in range(row-1, row+2):
                    for l in range(col-1, col+2):
                        hi = max(hi, grid[k][l])
                        
                ans[i][j] = hi
        
        return ans
