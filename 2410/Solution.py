from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        m = len(players)
        n = len(trainers)
        i = 0
        j = 0
        matched = 0

        while i < m and j < n:
            while j < n and players[i] > trainers[j]:
                j += 1

            if j < n:
                matched += 1

            i += 1
            j += 1

        return matched
