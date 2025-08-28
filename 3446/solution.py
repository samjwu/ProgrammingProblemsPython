from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        # main diagonal (\) and those below it
        for i in range(n):
            diagonal = [grid[i+j][j] for j in range(n - i)]
            diagonal.sort(reverse=True)
            for j in range(n - i):
                grid[i+j][j] = diagonal[j]

        # remaining diagonals above the main diagonal (\)
        for j in range(1, n):
            diagonal = [grid[i][i+j] for i in range(n - j)]
            diagonal.sort()
            for i in range(n - j):
                grid[i][j+i] = diagonal[i]

        return grid
