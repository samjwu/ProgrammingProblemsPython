class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        count_row = [0] * m
        count_col = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    count_row[i] += 1
                    count_col[j] += 1

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if count_row[i] > 1 or count_col[j] > 1:
                        ans += 1

        return ans
