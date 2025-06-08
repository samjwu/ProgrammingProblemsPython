from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        need = sum(apple)
        capacity.sort(reverse=True)
        idx = 0

        while need > 0:
            need -= capacity[idx]
            idx += 1

        return idx
