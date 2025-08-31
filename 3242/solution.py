from typing import List


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        n = len(grid)
        adj_dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        self.coordinate_sum = {}
        for i in range(n):
            for j in range(n):
                adj_sum = 0
                for x, y in adj_dirs:
                    new_i = i + x
                    new_j = j + y
                    if 0 <= new_i < n and 0 <= new_j < n:
                        adj_sum += grid[new_i][new_j]

                diag_sum = 0
                for x, y in diag_dirs:
                    new_i = i + x
                    new_j = j + y
                    if 0 <= new_i < n and 0 <= new_j < n:
                        diag_sum += grid[new_i][new_j]
            
                self.coordinate_sum[grid[i][j]] = (adj_sum, diag_sum)

    def adjacentSum(self, value: int) -> int:
        return self.coordinate_sum[value][0]

    def diagonalSum(self, value: int) -> int:
        return self.coordinate_sum[value][1]


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
