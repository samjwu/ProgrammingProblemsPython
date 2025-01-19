class Cell:
    def __init__(self, height, row, col):
        self.height = height
        self.row = row
        self.col = col

    # comparison method for min heap
    def __lt__(self, other):
        return self.height < other.height
        
class Solution:
    def trapRainWater(self, height_map):
        m = len(height_map)
        n = len(height_map[0])

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        visited = [[False for j in range(n)] for i in range(m)]

        min_heap = []

        # add outer ring left and right
        for i in range(m):
            heapq.heappush(min_heap, Cell(height_map[i][0], i, 0))
            visited[i][0] = True
            heapq.heappush(min_heap, Cell(height_map[i][n-1], i, n-1))
            visited[i][n-1] = True

        # add outer ring top and bot
        for i in range(n):
            heapq.heappush(min_heap, Cell(height_map[0][i], 0, i))
            visited[0][i] = True
            heapq.heappush(min_heap, Cell(height_map[m-1][i], m-1, i))
            visited[m-1][i] = True

        ans = 0

        # visit all cells, from lowest to highest height
        while min_heap:
            curr_cell = heapq.heappop(min_heap)

            curr_row = curr_cell.row
            curr_col = curr_cell.col
            min_height = curr_cell.height

            for direction in range(4):
                neighbor_row = curr_row + dx[direction]
                neighbor_col = curr_col + dy[direction]

                if (0 <= neighbor_row < m and 0 <= neighbor_col < n) and (not visited[neighbor_row][neighbor_col]):
                    neighbor_height = height_map[neighbor_row][neighbor_col]

                    # if neighbor is lower than current,
                    # can trap height difference in neighbor
                    if neighbor_height < min_height:
                        ans += min_height - neighbor_height

                    # effective height is the height we need to pretend the current neighbor height is for unvisited neighbors
                    # this simplifies needing to check for farthest boundaries
                    # eg: consider
                    # 9 9 9 9
                    # 9 1 2 9
                    # 9 3 4 9
                    # 9 9 9 9
                    # two cases:
                    # 1. neighbor_height < min_height, so effective_height = min_height
                    # 2. neighbor_height >= min_height, so effective_height = neighbor_height
                    effective_height = max(neighbor_height, min_height)

                    heapq.heappush(min_heap, Cell(effective_height, neighbor_row, neighbor_col))
                    visited[neighbor_row][neighbor_col] = True

        return ans
