class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # greedy: set first col to all 1
        for i in range(m):
            # flip row if first col is not 1
            if grid[i][0] == 0:
                for j in range(n):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0

        # greedy: maximizes 1s in cols, except first col
        for j in range(1, n):
            zeroes = 0
            
            for i in range(m):
                if grid[i][j] == 0:
                    zeroes += 1

            # flip col if more 0s than 1s
            if zeroes > m - zeroes:
                for i in range(m):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0

        ans = 0

        for i in range(m):
            for j in range(n):
                ans += grid[i][j] << (n-1 - j)
                
        return ans
