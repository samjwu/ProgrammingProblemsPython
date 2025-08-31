from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        dir_map = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }

        i = 0
        j = 0

        for command in commands:
            i += dir_map[command][0]
            j += dir_map[command][1]

        return i*n + j
