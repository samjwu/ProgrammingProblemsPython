class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        
        grid_sum = 0
        square_sum = 0
        
        for i in range(n):
            for j in range(n):
                grid_sum += grid[i][j]
                square_sum += grid[i][j]**2
                
        cells = n*n
        
        # sum from 1 to n = n(n+1)/2
        expected_grid_sum = cells * (cells + 1) // 2
        grid_sum_diff = grid_sum - expected_grid_sum

        # sum of squares from 1 to n = n(n+1)(2n+1)/6
        expected_square_sum = cells * (cells + 1) * (2 * cells + 1) // 6
        square_sum_diff = square_sum - expected_square_sum

        ans = [-1, -1]

        # let repeated = x, missing = y. then:
        # grid_sum_diff = x - y
        # square_sum_diff = x^2 - y^2
        # square_sum_diff / grid_sum_diff = (x^2 - y^2) / (x-y) = (x+y)
        # (x+y) + (x-y) = 2x
        ans[0] = ((square_sum_diff // grid_sum_diff) + grid_sum_diff) // 2
        # y = x - grid_sum_diff
        ans[1] = ans[0] - grid_sum_diff

        return ans
