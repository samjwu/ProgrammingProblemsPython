class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.MOD = 1e9 + 7
        
        self.memo = [[[-1 for k in range(maxMove+1)] for j in range(n)] for i in range(m)]
        
        def dfs(m: int, n: int, moves: int, i: int, j: int) -> int:
            if i == -1 or j == -1 or i == m or j == n:
                return 1
            
            if moves == 0:
                return 0
            
            if self.memo[i][j][moves] != -1:
                return self.memo[i][j][moves]
            
            subans = dfs(m, n, moves-1, i-1, j)
            subans += dfs(m, n, moves-1, i+1, j)
            subans %= self.MOD
            subans += dfs(m, n, moves-1, i, j-1)
            subans %= self.MOD
            subans += dfs(m, n, moves-1, i, j+1)
            subans %= self.MOD
            
            self.memo[i][j][moves] = subans
            
            return self.memo[i][j][moves]
        
        return dfs(m, n, maxMove, startRow, startColumn)
