class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        self.n = len(grid)

        self.grid = grid

        self.memo = [[-1 for col in range(self.n)] for row in range(self.n)]
        
        ans = inf

        for col in range(self.n):
            ans = min(ans, self.calc(0, col))
        
        return ans

    def calc(self, row: int, col: int) -> int:
        if row == self.n - 1:
            return self.grid[row][col]

        if self.memo[row][col] != -1:
            return self.memo[row][col]

        subans = inf

        for nextCol in range(self.n):
            if nextCol != col:
                subans = min(subans, self.calc(row + 1, nextCol))

        self.memo[row][col] = subans + self.grid[row][col]
        
        return self.memo[row][col]
