from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # track the minimum area of rectangle with all 1s
        # top left corner (min_row, min_col)
        # and bottom right corner (max_row, max_col)
        min_row = m
        max_row = 0
        min_col = n
        max_col = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)

        # add one to height and width since 0-indexed
        height = max_row - min_row + 1
        width = max_col - min_col + 1
        
        return height * width
