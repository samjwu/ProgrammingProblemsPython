class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = 0

        def dfs(grid: List[List[int]], m: int, n: int, i: int, j: int) -> int:
            if i < 0 or j < 0 or i == m or j == n or grid[i][j] == 0:
                return 0

            ans = 0

            # save value
            gold = grid[i][j]

            # mark visited
            grid[i][j] = 0

            for dx in range(-1, 2, 1):
                for dy in range(-1, 2, 1):
                    if abs(dx + dy) == 1:
                        ans = max(ans, dfs(grid, m, n, i + dx, j + dy))

            # backtrack
            grid[i][j] = gold

            return ans + gold

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(grid, m, n, i, j))

        return ans
