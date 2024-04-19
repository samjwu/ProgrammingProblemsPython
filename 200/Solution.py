class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        
        ans = 0
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    ans += 1
                    
        return ans

    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or j < 0 or i >= self.m or j >= self.n or grid[i][j] != "1":
            return
        
        grid[i][j] = '#'
        
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
