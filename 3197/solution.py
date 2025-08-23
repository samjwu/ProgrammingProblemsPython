from typing import List


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def minimumArea(grid: List[List[int]]) -> int:
            m = len(grid)
            n = len(grid[0])

            # track the minimum area of rectangle with all 1s
            # top left corner (min_row, min_col)
            # and bottom right corner (max_row, max_col)
            min_row = m
            max_row = 0
            min_col = n
            max_col = 0

            for row in range(m):
                for col in range(n):
                    if grid[row][col] == 1:
                        min_row = min(min_row, row)
                        max_row = max(max_row, row)
                        min_col = min(min_col, col)
                        max_col = max(max_col, col)

            # add one to height and width since 0-indexed
            height = max_row - min_row + 1
            width = max_col - min_col + 1
            
            return max(0, height * width)

        min_sum = inf

        # rotate the grid 90 degrees 3 times
        # to try at 0, 90, 180, 270 degrees
        for _ in range(4):
            # remeasure dimensions for each rotation
            m = len(grid)
            n = len(grid[0])

            for row in range(1, m):
                # take the top part to be the first rectangle
                rectangle1 = minimumArea(grid[:row])

                # split the bottom part vertically
                # try splitting at every column within bounds
                for col in range(1, m):
                    rectangle2 = minimumArea([rect[:col] for rect in grid[row:]])
                    rectangle3 = minimumArea([rect[col:] for rect in grid[row:]])
                    min_sum = min(min_sum, rectangle1 + rectangle2 + rectangle3)

                # split the bottom part horizontally
                # try splitting at every remaining row
                for remaining_row in range(row + 1, m):
                    rectangle2 = minimumArea(grid[row:remaining_row])
                    rectangle3 = minimumArea(grid[remaining_row:])
                    min_sum = min(min_sum, rectangle1 + rectangle2 + rectangle3)

            # perform rotation
            # first do vertical flip
            flipped = grid[::-1]
            # then transpose
            # converting rows into columns
            transposed = zip(*flipped)
            # finally return to list
            # resulting in 90 degree rotation
            grid = list(transposed)

        return min_sum
