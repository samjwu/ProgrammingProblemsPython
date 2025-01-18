class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        memo = [[float("inf") for j in range(n)] for i in range(m)]
        memo[0][0] = 0

        while True:
            # store current state to compare it to next state
            # if there is no change, answer is found
            prev_state = [row[:] for row in memo]

            # forward pass: check cells coming from left and top
            for row in range(m):
                for col in range(n):
                    # check cell above
                    if row > 0:
                        memo[row][col] = min(
                            memo[row][col],
                            memo[row - 1][col] + (0 if grid[row - 1][col] == 3 else 1),
                        )
                    # check cell to the left
                    if col > 0:
                        memo[row][col] = min(
                            memo[row][col],
                            memo[row][col - 1] + (0 if grid[row][col - 1] == 1 else 1),
                        )

            # backward pass: check cells coming from right and bottom
            for row in range(m - 1, -1, -1):
                for col in range(n - 1, -1, -1):
                    # check cell below
                    if row < m - 1:
                        memo[row][col] = min(
                            memo[row][col],
                            memo[row + 1][col] + (0 if grid[row + 1][col] == 4 else 1),
                        )
                    # check cell to the right
                    if col < n - 1:
                        memo[row][col] = min(
                            memo[row][col],
                            memo[row][col + 1] + (0 if grid[row][col + 1] == 2 else 1),
                        )

            # if no changes made, optimal paths all found
            if memo == prev_state:
                break

        return memo[m - 1][n - 1]
