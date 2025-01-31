class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        island_sizes = {}
        # 0 and 1 used by water and land
        island_id = 2

        # mark islands and sizes
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = self.dfs(grid, island_id, i, j, m, n)
                    island_id += 1

        if not island_sizes:
            return 1

        if len(island_sizes) == 1:
            island_id -= 1
            if island_sizes[island_id] == m * n:
                return island_sizes[island_id]
            else:
                # can add 1 land to island
                return island_sizes[island_id] + 1

        max_island_size = 1

        # try every water
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    current_island_size = 1
                    neighboring_islands = set()

                    if (i + 1 < m and grid[i + 1][j] > 1):
                        neighboring_islands.add(grid[i + 1][j])

                    if (i - 1 >= 0 and grid[i - 1][j] > 1):
                        neighboring_islands.add(grid[i - 1][j])

                    if (j + 1 < n and grid[i][j + 1] > 1):
                        neighboring_islands.add(grid[i][j + 1])

                    if (j - 1 >= 0 and grid[i][j - 1] > 1):
                        neighboring_islands.add(grid[i][j - 1])

                    for island_id in neighboring_islands:
                        current_island_size += island_sizes[island_id]
                        
                    max_island_size = max(max_island_size, current_island_size)

        return max_island_size

    # mark islands
    def dfs(self, grid: List[List[int]], island_id: int, i: int, j: int, m: int, n: int) -> int:
        if (
            i < 0 or i >= m
            or j < 0 or j >= n
            or grid[i][j] != 1
        ):
            return 0

        grid[i][j] = island_id

        return (
            1
            + self.dfs(grid, island_id, i + 1, j, m, n)
            + self.dfs(grid, island_id, i - 1, j, m, n)
            + self.dfs(grid, island_id, i, j + 1, m, n)
            + self.dfs(grid, island_id, i, j - 1, m, n)
        )
