class Solution:
    def __init__(self):
        self.PRIME = 60001
        self.DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = {x + self.PRIME * y for x, y in obstacles}

        x = 0
        y = 0

        ans = 0

        dir = 0

        for command in commands:
            if command == -1:
                dir = (dir + 1) % 4
                continue

            if command == -2:
                dir = (dir + 3) % 4
                continue

            dx, dy = self.DIRS[dir]
            for i in range(command):
                nextX = x + dx
                nextY = y + dy
                if nextX + self.PRIME * nextY in obstacles:
                    break
                x = nextX
                y = nextY

            ans = max(ans, x * x + y * y)

        return ans
