from typing import List

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        if not grid or not grid[0]:
            return False
            
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if (i < m-1 and grid[i][j] != grid[i+1][j]) or (j < n-1 and grid[i][j] == grid[i][j+1]):
                    return False

        return True
