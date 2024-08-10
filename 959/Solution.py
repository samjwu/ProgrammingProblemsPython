class Solution:
    DIRECTIONS = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]

    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        
        # increase grid size for identifying regions
        # multiply each cell by 3
        grid2 = [[0 for j in range(n*3)] for j in range(n*3)]

        for i in range(n):
            for j in range(n):
                newI = i*3
                newJ = j*3

                if grid[i][j] == "\\":
                    grid2[newI][newJ] = 1
                    grid2[newI+1][newJ+1] = 1
                    grid2[newI+2][newJ+2] = 1
                elif grid[i][j] == "/":
                    grid2[newI][newJ+2] = 1
                    grid2[newI+1][newJ+1] = 1
                    grid2[newI+2][newJ] = 1

        ans = 0
        
        for i in range(n*3):
            for j in range(n*3):
                if grid2[i][j] == 0:
                    self.floodFill(grid2, i, j)
                    ans += 1

        return ans

    def floodFill(self, grid2: List[List[int]], i: int, j: int) -> None:
        q = []
        q.append((i, j))

        grid2[i][j] = 1

        while q:
            curr = q.pop(0)
            
            for direction in self.DIRECTIONS:
                newI = curr[0] + direction[0]
                newJ = curr[1] + direction[1]
                
                if self.isUnvisited(grid2, newI, newJ):
                    grid2[newI][newJ] = 1
                    q.append((newI, newJ))

    def isUnvisited(self, grid2: List[List[int]], i: int, j: int) -> bool:
        n = len(grid2)

        return i >= 0 and i < n and j >= 0 and j < n and grid2[i][j] == 0
