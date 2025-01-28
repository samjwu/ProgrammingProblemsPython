class Solution:
    def dfs(self, grid, visited, row, col):
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[0])
            or grid[row][col] == 0
            or visited[row][col]
        ):
            return 0

        visited[row][col] = True

        return (
            grid[row][col]
            + self.dfs(grid, visited, row, col + 1)
            + self.dfs(grid, visited, row, col - 1)
            + self.dfs(grid, visited, row + 1, col)
            + self.dfs(grid, visited, row - 1, col)
        )

    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        visited = [[False] * n for i in range(m)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] > 0 and not visited[row][col]:
                    ans = max(ans, self.dfs(grid, visited, row, col))

        return ans
