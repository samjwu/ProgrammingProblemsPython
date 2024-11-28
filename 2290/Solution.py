class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        def isInBounds(row: int, col: int) -> bool:
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
        m = len(grid)
        n = len(grid[0])

        dists = [[float("inf") for j in range(n)] for i in range(m)]

        dists[0][0] = grid[0][0]

        # stores (distance, row, col)
        minHeap = [(dists[0][0], 0, 0)]

        while minHeap:
            dist, row, col = heapq.heappop(minHeap)

            # found answer with minimal obstacles
            if row == m - 1 and col == n - 1:
                return dist

            for direction in directions:
                nextRow = row + direction[0]
                nextCol = col + direction[1]

                if isInBounds(nextRow, nextCol):
                    nextDist = dist + grid[nextRow][nextCol]

                    # found path with less obstacles
                    if nextDist < dists[nextRow][nextCol]:
                        dists[nextRow][nextCol] = nextDist
                        heapq.heappush(minHeap, (nextDist, nextRow, nextCol))

        return dists[m-1][n-1]
