class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                white_cells = 0

                for di, dj in [(0, 0), (0, 1), (1, 0), (1, 1)]:
                    if grid[i + di][j + dj] == "W":
                        white_cells += 1
                
                if white_cells != 2:
                    return True

        return False
