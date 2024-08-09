class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)

        n = len(grid[0])
        
        ans = 0

        for i in range(m-2):
            for j in range(n-2):
                if self.isMagic(grid, i, j):
                    ans += 1

        return ans

    def isMagic(self, grid: List[List[int]], row: int, col: int) -> bool:
        seen = [False] * 10

        for i in range(3):
            for j in range(3):
                num = grid[row+i][col+j]

                if num < 1 or num > 9:
                    return False

                if seen[num]:
                    return False

                seen[num] = True

        diagonal1 = grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2]
        diagonal2 = grid[row+2][col] + grid[row+1][col+1] + grid[row][col+2]

        if diagonal1 != diagonal2:
            return False

        magicNum = diagonal1

        row1 = grid[row][col] + grid[row][col+1] + grid[row][col+2]
        row2 = grid[row+1][col] + grid[row+1][col+1] + grid[row+1][col+2]
        row3 = grid[row+2][col] + grid[row+2][col+1] + grid[row+2][col+2]
        
        if row1 != magicNum or row2 != magicNum or row3 != magicNum:
            return False

        col1 = grid[row][col] + grid[row+1][col] + grid[row+2][col]
        col2 = grid[row][col+1] + grid[row+1][col+1] + grid[row+2][col+1]
        col3 = grid[row][col+2] + grid[row+1][col+2] + grid[row+2][col+2]
        
        if col1 != magicNum or col2 != magicNum or col3 != magicNum:
            return False

        return True
