class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[[0 for i in range(n)] for j in range(n)] for k in range(m)]
        
        for row in range(m-1, -1, -1):
            for col1 in range(n):
                for col2 in range(n):
                    ans = grid[row][col1]
                    
                    if col1 != col2:
                        ans += grid[row][col2]
                        
                    if row != m-1:
                        maxCherry = 0
                        
                        for newcol1 in range(col1-1, col1+2, 1):
                            for newcol2 in range(col2-1, col2+2, 1):
                                if newcol1 >= 0 and newcol1 < n and newcol2 >= 0 and newcol2 < n:
                                    maxCherry = max(maxCherry, memo[row+1][newcol1][newcol2])
                        
                        ans += maxCherry
                                    
                    memo[row][col1][col2] = ans
                    
        return memo[0][0][n-1]
