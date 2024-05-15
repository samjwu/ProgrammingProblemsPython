class Solution:
    MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        self.n = len(grid)

        q = deque()

        # use -1 for empty
        # use 0 for thief
        # BFS starting from thief positions
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1

        # BFS and place min dist from thieves in grid
        while q:
            size = len(q)

            for i in range(size):
                curr = q.popleft()

                for move in self.MOVES:
                    nexti = curr[0] + move[0]
                    nextj = curr[1] + move[1]

                    if (
                        0 <= nexti < self.n
                        and 0 <= nextj < self.n
                        and grid[nexti][nextj] == -1
                    ):
                        grid[nexti][nextj] = grid[curr[0]][curr[1]] + 1
                        q.append((nexti, nextj))

        # binary search for ans
        minAns = 0
        maxAns = 0
        ans = -1

        for i in range(self.n):
            for j in range(self.n):
                maxAns = max(maxAns, grid[i][j])

        while minAns <= maxAns:
            mid = minAns + (maxAns - minAns) // 2

            if self.isPossibleAns(grid, mid):
                ans = mid
                minAns = mid + 1
            else:
                maxAns = mid - 1

        return ans

    # return True if minAns has a possible path, else return False
    def isPossibleAns(self, grid: List[List[int]], minAns: int) -> bool:
        if grid[0][0] < minAns or grid[self.n - 1][self.n - 1] < minAns:
            return False

        q = deque([(0, 0)])

        visited = [[False] * self.n for i in range(self.n)]
        visited[0][0] = True

        while q:
            curr = q.popleft()

            if curr[0] == self.n - 1 and curr[1] == self.n - 1:
                return True

            for move in self.MOVES:
                nexti = curr[0] + move[0]
                nextj = curr[1] + move[1]

                if (
                    0 <= nexti < self.n
                    and 0 <= nextj < self.n
                    and not visited[nexti][nextj]
                    and grid[nexti][nextj] >= minAns
                ):
                    visited[nexti][nextj] = True
                    q.append((nexti, nextj))

        return False
