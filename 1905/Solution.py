class Solution:
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def isSubIsland(self, x: int, y: int, grid1: List[List[int]], grid2: List[List[int]], visited: List[List[bool]]):
        """
        Starting at (x, y), do BFS on grid2
        while checking if islands in grid2 is subisland in grid1
        """
        m = len(grid2)
        n = len(grid2[0])

        isSubIsland = True

        q = deque()
        q.append((x, y))

        visited[x][y] = True

        while q:
            currX, currY = q.popleft()

            # if current cell is water in grid1
            # then grid2 island cannot be subisland of grid1
            if grid1[currX][currY] == 0:
                isSubIsland = False

            for direction in self.DIRS:
                nextX = currX + direction[0]
                nextY = currY + direction[1]
                
                # only add unvisited land cells to queue
                if (
                    0 <= nextX < m and 0 <= nextY < n
                    and not visited[nextX][nextY] and grid2[nextX][nextY] == 1
                ):
                    q.append((nextX, nextY))
                    visited[nextX][nextY] = True
                    
        return isSubIsland

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid2)
        n = len(grid2[0])

        visited = [[False for j in range(n)] for i in range(m)]

        ans = 0

        for x in range(m):
            for y in range(n):
                # do BFS check on unvisited land cells
                if (
                    not visited[x][y] and grid2[x][y] == 1
                    and self.isSubIsland(x, y, grid1, grid2, visited)
                ):
                    ans += 1

        return ans
