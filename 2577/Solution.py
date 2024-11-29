class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m = len(grid)
        n = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set()

        # stores (time, row, col)
        minHeap = [(grid[0][0], 0, 0)]

        while minHeap:
            time, row, col = heapq.heappop(minHeap)

            if row == m-1 and col == n-1:
                return time

            if (row, col) in visited:
                continue

            visited.add((row, col))

            for direction in directions:
                nextRow = row + direction[0]
                nextCol = col + direction[1]
                
                if nextRow < 0 or nextRow >= m or nextCol < 0 or nextCol >= n or (nextRow, nextCol) in visited:
                    continue

                # if time + 1 >= next cell, wait time is zero
                nextTime = time + 1

                # must wait if (time + 1 < next cell)
                # note the step itself takes 1 time unit
                # so if (next cell - time) is odd, wait time is the diff
                # and if (next cell - time) is even, wait time is the diff + 1
                wait = 0
                if time + 1 < grid[nextRow][nextCol]:
                    wait = grid[nextRow][nextCol]
                    wait += 0 if (grid[nextRow][nextCol] - time) % 2 else 1
                    nextTime = wait

                heapq.heappush(minHeap, (nextTime, nextRow, nextCol))

        return -1
