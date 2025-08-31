from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        ball_map = [[0 for j in range(11)] for i in range(n)]

        for player, ball in pick:
            ball_map[player][ball] += 1

        winners = 0

        for player in range(n):
            most = max(ball_map[player])
            if most > player:
                winners += 1

        return winners
