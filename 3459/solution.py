from functools import cache 
from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        m = len(grid)
        n = len(grid[0])

        @cache
        def dfs(curr_i: int, curr_j: int, direction: List[int], can_turn: bool, target: int) -> int:
            next_i = curr_i + directions[direction][0]
            next_j = curr_j + directions[direction][1]
            
            # must stay in bounds and move to valid target
            if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n or grid[next_i][next_j] != target:
                return 0
                
            # try stepping in same direction
            max_step = dfs(next_i, next_j, direction, can_turn, 2 - target)

            # try stepping after rotating 90 degrees clockwise
            if can_turn:
                max_step = max(
                    max_step,
                    dfs(next_i, next_j, (direction + 1) % 4, False, 2 - target),
                )

            # answer is the best of both options
            return max_step + 1

        longest = 0

        # try all possible starting points
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # try all possible starting directions
                    for direction in range(4):
                        longest = max(longest, dfs(i, j, direction, True, 2) + 1)

        return longest
