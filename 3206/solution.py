from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        alternating_groups = 0
        n = len(colors)

        for curr in range(n):
            prev = (curr - 1 + n) % n
            after = (curr + 1) % n

            if colors[prev] != colors[curr] and colors[curr] != colors[after]:
                alternating_groups += 1

        return alternating_groups
