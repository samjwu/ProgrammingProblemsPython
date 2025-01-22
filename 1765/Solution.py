class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        m = len(isWater)
        n = len(isWater[0])

        def is_in_bounds(x, y):
            return 0 <= x < m and 0 <= y < n

        ans = [[-1 for _ in range(n)] for _ in range(m)]

        q = deque()

        for x in range(m):
            for y in range(n):
                if isWater[x][y] == 1:
                    q.append((x, y))
                    ans[x][y] = 0

        height = 1

        while q:
            k = len(q)

            for _ in range(k):
                cur = q.popleft()

                for d in range(4):
                    neighbor_x = cur[0] + dx[d]
                    neighbor_y = cur[1] + dy[d]

                    if (
                        is_in_bounds(neighbor_x, neighbor_y)
                        and ans[neighbor_x][neighbor_y] == -1
                    ):
                        ans[neighbor_x][neighbor_y] = height
                        q.append((neighbor_x, neighbor_y))

            height += 1

        return ans
