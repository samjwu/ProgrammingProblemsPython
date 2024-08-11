class Solution:
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def minDays(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def numIslands():
            visited = set()

            ans = 0

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        floodFill(i, j, visited)
                        ans += 1

            return ans

        def floodFill(i: int, j: int, visited: set[tuple[int]]):
            if (
                i < 0 or i >= m
                or j < 0 or j >= n
                or grid[i][j] == 0
                or (i, j) in visited
            ):
                return

            visited.add((i, j))

            for dir in self.DIRECTIONS:
                floodFill(i + dir[0], j + dir[1], visited)

        # already disconnected
        if numIslands() != 1:
            return 0

        # try converting each individual land to water
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # convert
                    grid[i][j] = 0

                    # successfully disconnected
                    if numIslands() != 1:
                        return 1

                    # backtrack
                    grid[i][j] = 1

        # at most 2 days needed
        return 2
